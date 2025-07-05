/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2019, PickNik Inc.
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of PickNik Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *********************************************************************/

/* Author: Henning Kayser */

#include <stdexcept>

#include <moveit/controller_manager/controller_manager.h>
#include <moveit/moveit_cpp/moveit_cpp.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.hpp>
#include <geometry_msgs/msg/quaternion_stamped.hpp>

namespace moveit_cpp
{
static const rclcpp::Logger LOGGER = rclcpp::get_logger("moveit.ros_planning_interface.moveit_cpp");
constexpr char PLANNING_PLUGIN_PARAM[] = "planning_plugin";

MoveItCpp::MoveItCpp(const rclcpp::Node::SharedPtr& node) : MoveItCpp(node, Options(node))
{
}

MoveItCpp::MoveItCpp(const rclcpp::Node::SharedPtr& node, const Options& options) : node_(node)
{
  // Configure planning scene monitor
  if (!loadPlanningSceneMonitor(options.planning_scene_monitor_options))
  {
    const std::string error = "Unable to configure planning scene monitor";
    RCLCPP_FATAL_STREAM(LOGGER, error);
    throw std::runtime_error(error);
  }

  robot_model_ = planning_scene_monitor_->getRobotModel();
  if (!robot_model_)
  {
    const std::string error = "Unable to construct robot model. Please make sure all needed information is on the "
                              "parameter server.";
    RCLCPP_FATAL_STREAM(LOGGER, error);
    throw std::runtime_error(error);
  }

  bool load_planning_pipelines = true;
  if (load_planning_pipelines && !loadPlanningPipelines(options.planning_pipeline_options))
  {
    const std::string error = "Failed to load planning pipelines from parameter server";
    RCLCPP_FATAL_STREAM(LOGGER, error);
    throw std::runtime_error(error);
  }

  trajectory_execution_manager_ = std::make_shared<trajectory_execution_manager::TrajectoryExecutionManager>(
      node_, robot_model_, planning_scene_monitor_->getStateMonitor());

  RCLCPP_DEBUG(LOGGER, "MoveItCpp running");
}

MoveItCpp::~MoveItCpp()
{
  RCLCPP_INFO(LOGGER, "Deleting MoveItCpp");
  clearContents();
}

bool MoveItCpp::loadPlanningSceneMonitor(const PlanningSceneMonitorOptions& options)
{
  planning_scene_monitor_ =
      std::make_shared<planning_scene_monitor::PlanningSceneMonitor>(node_, options.robot_description, options.name);
  // Allows us to synchronize to Rviz and also publish collision objects to ourselves
  RCLCPP_DEBUG(LOGGER, "Configuring Planning Scene Monitor");
  if (planning_scene_monitor_->getPlanningScene())
  {
    // Start state and scene monitors
    RCLCPP_INFO(LOGGER, "Listening to '%s' for joint states", options.joint_state_topic.c_str());
    // Subscribe to JointState sensor messages
    planning_scene_monitor_->startStateMonitor(options.joint_state_topic, options.attached_collision_object_topic);
    // Publish planning scene updates to remote monitors like RViz
    planning_scene_monitor_->startPublishingPlanningScene(planning_scene_monitor::PlanningSceneMonitor::UPDATE_SCENE,
                                                          options.monitored_planning_scene_topic);
    // Monitor and apply planning scene updates from remote publishers like the PlanningSceneInterface
    planning_scene_monitor_->startSceneMonitor(options.publish_planning_scene_topic);
    // Monitor requests for changes in the collision environment
    planning_scene_monitor_->startWorldGeometryMonitor();
  }
  else
  {
    RCLCPP_ERROR(LOGGER, "Planning scene not configured");
    return false;
  }

  // Wait for complete state to be received
  if (options.wait_for_initial_state_timeout > 0.0)
  {
    return planning_scene_monitor_->getStateMonitor()->waitForCurrentState(node_->now(),
                                                                           options.wait_for_initial_state_timeout);
  }

  return true;
}

bool MoveItCpp::loadPlanningPipelines(const PlanningPipelineOptions& options)
{
  // TODO(henningkayser): Use parent namespace for planning pipeline config lookup
  // ros::NodeHandle node_handle(options.parent_namespace.empty() ? "~" : options.parent_namespace);
  for (const auto& planning_pipeline_name : options.pipeline_names)
  {
    if (planning_pipelines_.count(planning_pipeline_name) > 0)
    {
      RCLCPP_WARN(LOGGER, "Skipping duplicate entry for planning pipeline '%s'.", planning_pipeline_name.c_str());
      continue;
    }
    RCLCPP_INFO(LOGGER, "Loading planning pipeline '%s'", planning_pipeline_name.c_str());
    planning_pipeline::PlanningPipelinePtr pipeline;
    pipeline = std::make_shared<planning_pipeline::PlanningPipeline>(robot_model_, node_, planning_pipeline_name,
                                                                     PLANNING_PLUGIN_PARAM);

    if (!pipeline->getPlannerManager())
    {
      RCLCPP_ERROR(LOGGER, "Failed to initialize planning pipeline '%s'.", planning_pipeline_name.c_str());
      continue;
    }

    planning_pipelines_[planning_pipeline_name] = pipeline;
  }

  if (planning_pipelines_.empty())
  {
    RCLCPP_ERROR(LOGGER, "Failed to load any planning pipelines.");
    return false;
  }

  // Retrieve group/pipeline mapping for faster lookup
  std::vector<std::string> group_names = robot_model_->getJointModelGroupNames();
  for (const auto& pipeline_entry : planning_pipelines_)
  {
    for (const auto& group_name : group_names)
    {
      const auto& pipeline = pipeline_entry.second;
      for (const auto& planner_configuration : pipeline->getPlannerManager()->getPlannerConfigurations())
      {
        if (planner_configuration.second.group == group_name)
        {
          groups_pipelines_map_[group_name].insert(pipeline_entry.first);
        }
      }
    }
  }

  return true;
}

moveit::core::RobotModelConstPtr MoveItCpp::getRobotModel() const
{
  return robot_model_;
}

const rclcpp::Node::SharedPtr& MoveItCpp::getNode() const
{
  return node_;
}

bool MoveItCpp::getCurrentState(moveit::core::RobotStatePtr& current_state, double wait_seconds)
{
  if (wait_seconds > 0.0 && !planning_scene_monitor_->getStateMonitor()->waitForCurrentState(node_->now(), wait_seconds))
  {
    RCLCPP_ERROR(LOGGER, "Did not receive robot state");
    return false;
  }
  {  // Lock planning scene
    planning_scene_monitor::LockedPlanningSceneRO scene(planning_scene_monitor_);
    current_state = std::make_shared<moveit::core::RobotState>(scene->getCurrentState());
  }  // Unlock planning scene
  return true;
}

moveit::core::RobotStatePtr MoveItCpp::getCurrentState(double wait)
{
  moveit::core::RobotStatePtr current_state;
  getCurrentState(current_state, wait);
  return current_state;
}

const std::map<std::string, planning_pipeline::PlanningPipelinePtr>& MoveItCpp::getPlanningPipelines() const
{
  return planning_pipelines_;
}

std::set<std::string> MoveItCpp::getPlanningPipelineNames(const std::string& group_name) const
{
  if (group_name.empty() || groups_pipelines_map_.count(group_name) == 0)
  {
    RCLCPP_ERROR(LOGGER, "No planning pipelines loaded for group '%s'. Check planning pipeline and controller setup.",
                 group_name.c_str());
    return {};  // empty
  }

  return groups_pipelines_map_.at(group_name);
}

const planning_scene_monitor::PlanningSceneMonitorPtr& MoveItCpp::getPlanningSceneMonitor() const
{
  return planning_scene_monitor_;
}

planning_scene_monitor::PlanningSceneMonitorPtr MoveItCpp::getPlanningSceneMonitorNonConst()
{
  return planning_scene_monitor_;
}

const trajectory_execution_manager::TrajectoryExecutionManagerPtr& MoveItCpp::getTrajectoryExecutionManager() const
{
  return trajectory_execution_manager_;
}

trajectory_execution_manager::TrajectoryExecutionManagerPtr MoveItCpp::getTrajectoryExecutionManagerNonConst()
{
  return trajectory_execution_manager_;
}

moveit_controller_manager::ExecutionStatus
MoveItCpp::execute(const std::string& group_name, const robot_trajectory::RobotTrajectoryPtr& robot_trajectory,
                   bool blocking)
{
  if (!robot_trajectory)
  {
    RCLCPP_ERROR(LOGGER, "Robot trajectory is undefined");
    return moveit_controller_manager::ExecutionStatus::ABORTED;
  }

  // Check if there are controllers that can handle the execution
  if (!trajectory_execution_manager_->ensureActiveControllersForGroup(group_name))
  {
    RCLCPP_ERROR(LOGGER, "Execution failed! No active controllers configured for group '%s'", group_name.c_str());
    return moveit_controller_manager::ExecutionStatus::ABORTED;
  }

  // Execute trajectory
  moveit_msgs::msg::RobotTrajectory robot_trajectory_msg;
  robot_trajectory->getRobotTrajectoryMsg(robot_trajectory_msg);
  if (blocking)
  {
    trajectory_execution_manager_->push(robot_trajectory_msg);
    trajectory_execution_manager_->execute();
    return trajectory_execution_manager_->waitForExecution();
  }
  trajectory_execution_manager_->pushAndExecute(robot_trajectory_msg);
  return moveit_controller_manager::ExecutionStatus::RUNNING;
}

const std::shared_ptr<tf2_ros::Buffer>& MoveItCpp::getTFBuffer() const
{
  return planning_scene_monitor_->getTFClient();
}

void MoveItCpp::clearContents()
{
  planning_scene_monitor_.reset();
  robot_model_.reset();
  planning_pipelines_.clear();
}
}  // namespace moveit_cpp
