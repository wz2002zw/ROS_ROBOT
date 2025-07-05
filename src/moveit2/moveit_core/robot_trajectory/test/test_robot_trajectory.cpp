/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2013, Willow Garage, Inc.
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
 *   * Neither the name of the Willow Garage nor the names of its
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

/* Author: Ioan Sucan */

#include <moveit/robot_model/robot_model.h>
#include <moveit/robot_state/robot_state.h>
#include <moveit/robot_trajectory/robot_trajectory.h>
#include <moveit/utils/robot_model_test_utils.h>
#include <gtest/gtest.h>

class RobotTrajectoryTestFixture : public testing::Test
{
protected:
  moveit::core::RobotModelConstPtr robot_model_;
  moveit::core::RobotStatePtr robot_state_;
  const std::string robot_model_name_ = "panda";
  const std::string arm_jmg_name_ = "panda_arm";
  const std::string arm_state_name_ = "ready";

protected:
  void SetUp() override
  {
    robot_model_ = moveit::core::loadTestingRobotModel(robot_model_name_);
    robot_state_ = std::make_shared<moveit::core::RobotState>(robot_model_);
    robot_state_->setToDefaultValues();
    robot_state_->setVariableVelocity(/*index*/ 0, /*value*/ 1.0);
    robot_state_->setVariableAcceleration(/*index*/ 0, /*value*/ -0.1);
    robot_state_->update();
  }

  void TearDown() override
  {
  }

  void initTestTrajectory(robot_trajectory::RobotTrajectoryPtr& trajectory)
  {
    // Init a trajectory
    ASSERT_TRUE(robot_model_->hasJointModelGroup(arm_jmg_name_))
        << "Robot model does not have group: " << arm_jmg_name_;

    trajectory = std::make_shared<robot_trajectory::RobotTrajectory>(robot_model_, arm_jmg_name_);

    EXPECT_EQ(trajectory->getGroupName(), arm_jmg_name_) << "Generated trajectory group name does not match";
    EXPECT_TRUE(trajectory->empty()) << "Generated trajectory not empty";

    double duration_from_previous = 0.1;
    std::size_t waypoint_count = 5;
    for (std::size_t ix = 0; ix < waypoint_count; ++ix)
    {
      trajectory->addSuffixWayPoint(*robot_state_, duration_from_previous);
    }

    // Quick check that getDuration is working correctly
    EXPECT_EQ(trajectory->getDuration(), duration_from_previous * waypoint_count)
        << "Generated trajectory duration incorrect";
    EXPECT_EQ(waypoint_count, trajectory->getWayPointDurations().size())
        << "Generated trajectory has the wrong number of waypoints";
    EXPECT_EQ(waypoint_count, trajectory->size());
  }

  void copyTrajectory(const robot_trajectory::RobotTrajectoryPtr& trajectory,
                      robot_trajectory::RobotTrajectoryPtr& trajectory_copy, bool deepcopy)
  {
    // Copy the trajectory
    trajectory_copy = std::make_shared<robot_trajectory::RobotTrajectory>(*trajectory, deepcopy);
    // Quick check that the getDuration values match
    EXPECT_EQ(trajectory_copy->getDuration(), trajectory->getDuration());
    EXPECT_EQ(trajectory_copy->getWayPointDurations().size(), trajectory->getWayPointDurations().size());
  }

  void modifyFirstWaypointPtrAndCheckTrajectory(robot_trajectory::RobotTrajectoryPtr& trajectory)
  {
    ///////////////////////////
    // Get the first waypoint by POINTER, modify it, and check that the value WAS updated in trajectory
    ///////////////////////////
    // Get the first waypoint by shared pointer
    moveit::core::RobotStatePtr trajectory_first_waypoint = trajectory->getWayPointPtr(0);
    // Get the first waypoint joint values
    std::vector<double> trajectory_first_state;
    trajectory_first_waypoint->copyJointGroupPositions(arm_jmg_name_, trajectory_first_state);

    // Modify the first waypoint joint values
    trajectory_first_state[0] += 0.01;
    trajectory_first_waypoint->setJointGroupPositions(arm_jmg_name_, trajectory_first_state);

    // Check that the trajectory's first waypoint was updated
    moveit::core::RobotStatePtr trajectory_first_waypoint_after_update = trajectory->getWayPointPtr(0);
    std::vector<double> trajectory_first_state_after_update;
    trajectory_first_waypoint_after_update->copyJointGroupPositions(arm_jmg_name_, trajectory_first_state_after_update);
    EXPECT_EQ(trajectory_first_state[0], trajectory_first_state_after_update[0]);

    // Modify the first waypoint duration
    double trajectory_first_duration_before_update = trajectory->getWayPointDurationFromPrevious(0);
    double new_duration = trajectory_first_duration_before_update + 0.1;
    trajectory->setWayPointDurationFromPrevious(0, new_duration);

    // Check that the trajectory's first duration was updated
    EXPECT_EQ(trajectory->getWayPointDurationFromPrevious(0), new_duration);
  }

  void modifyFirstWaypointAndCheckTrajectory(robot_trajectory::RobotTrajectoryPtr& trajectory)
  {
    ///////////////////////////
    // Get the first waypoint by VALUE, modify it, and check that the value WAS NOT updated in trajectory
    ///////////////////////////
    // Get the first waypoint by shared pointer
    moveit::core::RobotState trajectory_first_waypoint = trajectory->getWayPoint(0);
    // Get the first waypoint joint values
    std::vector<double> trajectory_first_state;
    trajectory_first_waypoint.copyJointGroupPositions(arm_jmg_name_, trajectory_first_state);

    // Modify the first waypoint joint values
    trajectory_first_state[0] += 0.01;
    trajectory_first_waypoint.setJointGroupPositions(arm_jmg_name_, trajectory_first_state);

    // Check that the trajectory's first waypoint was updated
    moveit::core::RobotState trajectory_first_waypoint_after_update = trajectory->getWayPoint(0);
    std::vector<double> trajectory_first_state_after_update;
    trajectory_first_waypoint_after_update.copyJointGroupPositions(arm_jmg_name_, trajectory_first_state_after_update);
    EXPECT_NE(trajectory_first_state[0], trajectory_first_state_after_update[0]);
  }
};

TEST_F(RobotTrajectoryTestFixture, ModifyFirstWaypointByPtr)
{
  robot_trajectory::RobotTrajectoryPtr trajectory;
  initTestTrajectory(trajectory);
  modifyFirstWaypointPtrAndCheckTrajectory(trajectory);
}

TEST_F(RobotTrajectoryTestFixture, ModifyFirstWaypointByValue)
{
  robot_trajectory::RobotTrajectoryPtr trajectory;
  initTestTrajectory(trajectory);
  modifyFirstWaypointAndCheckTrajectory(trajectory);
}

TEST_F(RobotTrajectoryTestFixture, DoubleReverse)
{
  robot_trajectory::RobotTrajectoryPtr trajectory;
  initTestTrajectory(trajectory);
  moveit_msgs::msg::RobotTrajectory initial_trajectory_msg;
  trajectory->getRobotTrajectoryMsg(initial_trajectory_msg);

  trajectory->reverse().reverse();

  moveit_msgs::msg::RobotTrajectory edited_trajectory_msg;
  trajectory->getRobotTrajectoryMsg(edited_trajectory_msg);

  EXPECT_EQ(initial_trajectory_msg, edited_trajectory_msg);
}

TEST_F(RobotTrajectoryTestFixture, ChainEdits)
{
  robot_trajectory::RobotTrajectoryPtr initial_trajectory;
  initTestTrajectory(initial_trajectory);
  moveit_msgs::msg::RobotTrajectory initial_trajectory_msg;
  initial_trajectory->getRobotTrajectoryMsg(initial_trajectory_msg);

  robot_trajectory::RobotTrajectory trajectory(robot_model_);
  trajectory.setGroupName(arm_jmg_name_)
      .clear()
      .setRobotTrajectoryMsg(*robot_state_, initial_trajectory_msg)
      .reverse()
      .addSuffixWayPoint(*robot_state_, 0.1)
      .addPrefixWayPoint(*robot_state_, 0.1)
      .insertWayPoint(1, *robot_state_, 0.1)
      .append(*initial_trajectory, 0.1);

  EXPECT_EQ(trajectory.getGroupName(), arm_jmg_name_);
  EXPECT_EQ(trajectory.getWayPointCount(), initial_trajectory->getWayPointCount() * 2 + 3);
}

TEST_F(RobotTrajectoryTestFixture, Append)
{
  robot_trajectory::RobotTrajectoryPtr initial_trajectory;
  initTestTrajectory(initial_trajectory);
  EXPECT_EQ(initial_trajectory->getWayPointCount(), size_t(5));

  // Append to the first
  robot_trajectory::RobotTrajectoryPtr traj2;
  initTestTrajectory(traj2);
  EXPECT_EQ(traj2->getWayPointCount(), size_t(5));

  // After append() we should have 10 waypoints, all with 0.1s duration
  const double expected_duration = 0.1;
  initial_trajectory->append(*traj2, expected_duration, 0, 5);
  EXPECT_EQ(initial_trajectory->getWayPointCount(), size_t(10));

  EXPECT_EQ(initial_trajectory->getWayPointDurationFromPrevious(4), expected_duration);
  EXPECT_EQ(initial_trajectory->getWayPointDurationFromPrevious(5), expected_duration);
  EXPECT_EQ(initial_trajectory->getWayPointDurationFromPrevious(6), expected_duration);
}

TEST_F(RobotTrajectoryTestFixture, RobotTrajectoryShallowCopy)
{
  bool deepcopy = false;

  robot_trajectory::RobotTrajectoryPtr trajectory;
  robot_trajectory::RobotTrajectoryPtr trajectory_copy;

  initTestTrajectory(trajectory);
  copyTrajectory(trajectory, trajectory_copy, deepcopy);
  modifyFirstWaypointPtrAndCheckTrajectory(trajectory);

  // Check that modifying the waypoint also modified the trajectory
  moveit::core::RobotState trajectory_first_waypoint_after_update = trajectory->getWayPoint(0);
  std::vector<double> trajectory_first_state_after_update;
  trajectory_first_waypoint_after_update.copyJointGroupPositions(arm_jmg_name_, trajectory_first_state_after_update);

  // Get the first waypoint in the modified trajectory_copy
  moveit::core::RobotState trajectory_copy_first_waypoint_after_update = trajectory_copy->getWayPoint(0);
  std::vector<double> trajectory_copy_first_state_after_update;
  trajectory_copy_first_waypoint_after_update.copyJointGroupPositions(arm_jmg_name_,
                                                                      trajectory_copy_first_state_after_update);

  // Check that we updated the joint position correctly in the trajectory
  EXPECT_EQ(trajectory_first_state_after_update[0], trajectory_copy_first_state_after_update[0]);
}

TEST_F(RobotTrajectoryTestFixture, RobotTrajectoryDeepCopy)
{
  bool deepcopy = true;

  robot_trajectory::RobotTrajectoryPtr trajectory;
  robot_trajectory::RobotTrajectoryPtr trajectory_copy;

  initTestTrajectory(trajectory);
  copyTrajectory(trajectory, trajectory_copy, deepcopy);
  modifyFirstWaypointPtrAndCheckTrajectory(trajectory);

  // Check that modifying the waypoint also modified the trajectory
  moveit::core::RobotState trajectory_first_waypoint_after_update = trajectory->getWayPoint(0);
  std::vector<double> trajectory_first_state_after_update;
  trajectory_first_waypoint_after_update.copyJointGroupPositions(arm_jmg_name_, trajectory_first_state_after_update);

  // Get the first waypoint in the modified trajectory_copy
  moveit::core::RobotState trajectory_copy_first_waypoint_after_update = trajectory_copy->getWayPoint(0);
  std::vector<double> trajectory_copy_first_state_after_update;
  trajectory_copy_first_waypoint_after_update.copyJointGroupPositions(arm_jmg_name_,
                                                                      trajectory_copy_first_state_after_update);

  // Check that joint positions changed in the original trajectory but not the deep copy
  EXPECT_NE(trajectory_first_state_after_update[0], trajectory_copy_first_state_after_update[0]);
  // Check that the first waypoint duration changed in the original trajectory but not the deep copy
  EXPECT_NE(trajectory->getWayPointDurationFromPrevious(0), trajectory_copy->getWayPointDurationFromPrevious(0));
}

TEST_F(RobotTrajectoryTestFixture, RobotTrajectoryIterator)
{
  robot_trajectory::RobotTrajectoryPtr trajectory;
  initTestTrajectory(trajectory);

  ASSERT_EQ(5u, trajectory->size());
  std::vector<double> positions;

  double start_pos = 0.0;

  for (size_t i = 0; i < trajectory->size(); ++i)
  {
    auto waypoint = trajectory->getWayPointPtr(i);
    // modify joint values
    waypoint->copyJointGroupPositions(arm_jmg_name_, positions);
    start_pos = positions[0];
    positions[0] += 0.01 * i;
    waypoint->setJointGroupPositions(arm_jmg_name_, positions);
  }

  unsigned int count = 0;
  for (const auto& waypoint_and_duration : *trajectory)
  {
    const auto& waypoint = waypoint_and_duration.first;
    waypoint->copyJointGroupPositions(arm_jmg_name_, positions);
    EXPECT_EQ(start_pos + count * 0.01, positions[0]);
    count++;
  }

  EXPECT_EQ(count, trajectory->size());

  // Consistency checks
  EXPECT_EQ(trajectory->begin(), trajectory->begin());
  EXPECT_EQ(trajectory->end(), trajectory->end());

  // trajectory has length 5; incrementing begin 5 times should reach the end
  EXPECT_NE(trajectory->begin(), trajectory->end());
  EXPECT_NE(++trajectory->begin(), trajectory->end());
  EXPECT_NE(++(++trajectory->begin()), trajectory->end());
  EXPECT_NE(++(++(++trajectory->begin())), trajectory->end());
  EXPECT_NE(++(++(++(++trajectory->begin()))), trajectory->end());
  EXPECT_EQ(++(++(++(++(++trajectory->begin())))), trajectory->end());
}

TEST_F(RobotTrajectoryTestFixture, RobotTrajectoryLength)
{
  robot_trajectory::RobotTrajectoryPtr trajectory;
  initTestTrajectory(trajectory);
  EXPECT_FLOAT_EQ(robot_trajectory::path_length(*trajectory), 0.0);

  // modify joint values so the smoothness is nonzero
  std::vector<double> positions;
  for (size_t i = 0; i < trajectory->size(); ++i)
  {
    auto waypoint = trajectory->getWayPointPtr(i);
    waypoint->copyJointGroupPositions(arm_jmg_name_, positions);
    positions[0] += 0.01 * i;
    waypoint->setJointGroupPositions(arm_jmg_name_, positions);
  }
  EXPECT_GT(robot_trajectory::path_length(*trajectory), 0.0);
}

TEST_F(RobotTrajectoryTestFixture, RobotTrajectorySmoothness)
{
  robot_trajectory::RobotTrajectoryPtr trajectory;
  initTestTrajectory(trajectory);

  // modify joint values so the smoothness is nonzero
  std::vector<double> positions;
  for (size_t i = 0; i < trajectory->size(); ++i)
  {
    auto waypoint = trajectory->getWayPointPtr(i);
    waypoint->copyJointGroupPositions(arm_jmg_name_, positions);
    positions[0] += 0.01 * i;
    waypoint->setJointGroupPositions(arm_jmg_name_, positions);
  }

  const auto smoothness = robot_trajectory::smoothness(*trajectory);
  ASSERT_TRUE(smoothness.has_value());
  EXPECT_GT(smoothness.value(), 0.0);

  // Check for empty trajectory
  trajectory->clear();
  EXPECT_FALSE(robot_trajectory::smoothness(*trajectory).has_value());
}

TEST_F(RobotTrajectoryTestFixture, RobotTrajectoryDensity)
{
  robot_trajectory::RobotTrajectoryPtr trajectory;
  initTestTrajectory(trajectory);

  // If trajectory has all equal state, and length zero, density should be null.
  auto density = robot_trajectory::waypoint_density(*trajectory);
  ASSERT_FALSE(density.has_value());

  // modify joint values so the density is nonzero
  std::vector<double> positions;
  for (size_t i = 0; i < trajectory->size(); ++i)
  {
    auto waypoint = trajectory->getWayPointPtr(i);
    waypoint->copyJointGroupPositions(arm_jmg_name_, positions);
    positions[0] += 0.01 * i;
    waypoint->setJointGroupPositions(arm_jmg_name_, positions);
  }

  density = robot_trajectory::waypoint_density(*trajectory);
  ASSERT_TRUE(density.has_value());
  EXPECT_GT(density.value(), 0.0);

  // Check for empty trajectory
  trajectory->clear();
  density = robot_trajectory::waypoint_density(*trajectory);
  EXPECT_FALSE(density.has_value());
}

int main(int argc, char** argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
