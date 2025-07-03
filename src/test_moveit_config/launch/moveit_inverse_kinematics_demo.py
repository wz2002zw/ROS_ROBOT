#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from moveit_commander import RobotCommander, MoveGroupCommander
from moveit_commander import PlanningSceneInterface
from geometry_msgs.msg import Pose
from tf_transformations import quaternion_from_euler
import numpy as np

class MoveItIKDemo(Node):
    def __init__(self):
        super().__init__('moveit_ik_demo')
        
        # 初始化MoveIt接口
        rclpy.init(args=sys.argv)
        self.robot = RobotCommander()
        self.scene = PlanningSceneInterface()
        
        # 创建规划组（根据你的SRDF修改）
        self.group_name = "manipulator"  # 对应srdf中的规划组名称
        self.move_group = MoveGroupCommander(self.group_name)
        
        # 设置规划参数
        self.move_group.set_planning_time(5.0)  # 规划超时时间（秒）
        self.move_group.set_num_planning_attempts(5)  # 规划尝试次数
        self.move_group.set_goal_position_tolerance(0.01)  # 位置容差（米）
        self.move_group.set_goal_orientation_tolerance(0.01)  # 姿态容差（弧度）
        
        # 打印机械臂信息
        self.get_logger().info(f"可用规划组: {self.robot.get_group_names()}")
        self.get_logger().info(f"当前规划组: {self.group_name}")
        self.get_logger().info(f"末端执行器: {self.move_group.get_end_effector_link()}")
        
        # 预定义测试位姿
        self.test_poses = self._create_test_poses()
    
    def _create_test_poses(self):
        """创建几个测试位姿用于逆运动学测试"""
        poses = []
        
        # 位姿1: 前方位置，垂直向下姿态
        pose1 = Pose()
        pose1.position.x = 0.4
        pose1.position.y = 0.0
        pose1.position.z = 0.4
        q = quaternion_from_euler(0, np.pi/2, 0)  # 垂直向下
        pose1.orientation.x = q[0]
        pose1.orientation.y = q[1]
        pose1.orientation.z = q[2]
        pose1.orientation.w = q[3]
        poses.append(pose1)
        
        # 位姿2: 侧方位置，水平姿态
        pose2 = Pose()
        pose2.position.x = 0.2
        pose2.position.y = 0.3
        pose2.position.z = 0.3
        q = quaternion_from_euler(0, 0, np.pi/2)  # 水平朝向
        pose2.orientation.x = q[0]
        pose2.orientation.y = q[1]
        pose2.orientation.z = q[2]
        pose2.orientation.w = q[3]
        poses.append(pose2)
        
        return poses
    
    def run_demo(self):
        """运行逆运动学测试Demo"""
        self.get_logger().info("=== 开始MoveIt逆运动学测试Demo ===")
        
        # 先移动到初始姿态（可选）
        self.get_logger().info("移动到初始姿态...")
        self.move_group.set_named_target("home")  # 需要在SRDF中定义
        success = self.move_group.go(wait=True)
        if not success:
            self.get_logger().warn("无法移动到初始姿态，继续测试...")
        
        # 测试预定义的位姿
        for i, pose in enumerate(self.test_poses):
            self.get_logger().info(f"\n=== 测试位姿 {i+1} ===")
            self.get_logger().info(f"目标位置: ({pose.position.x:.3f}, {pose.position.y:.3f}, {pose.position.z:.3f})")
            self.get_logger().info(f"目标姿态: 四元数 ({pose.orientation.x:.3f}, {pose.orientation.y:.3f}, {pose.orientation.z:.3f}, {pose.orientation.w:.3f})")
            
            # 设置目标位姿并调用逆运动学
            self.move_group.set_pose_target(pose)
            
            # 计算运动规划
            self.get_logger().info("正在规划轨迹...")
            plan = self.move_group.plan()
            
            if len(plan.joint_trajectory.points) > 0:
                self.get_logger().info("逆运动学求解成功！轨迹包含 {} 个点".format(
                    len(plan.joint_trajectory.points)))
                
                # 打印最终关节角度
                final_joint_values = plan.joint_trajectory.points[-1].positions
                joint_names = plan.joint_trajectory.joint_names
                self.get_logger().info("最终关节角度:")
                for name, value in zip(joint_names, final_joint_values):
                    self.get_logger().info(f"  {name}: {value:.3f} rad")
                
                # 执行轨迹（取消注释此行以实际执行）
                # self.get_logger().info("执行轨迹...")
                # self.move_group.execute(plan)
                
            else:
                self.get_logger().error("逆运动学求解失败！可能超出工作空间或存在碰撞")
            
            # 等待用户输入继续下一个测试
            input("\n按Enter继续下一个测试...")
        
        self.get_logger().info("=== 逆运动学测试Demo完成 ===")

def main(args=None):
    try:
        demo = MoveItIKDemo()
        demo.run_demo()
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    main()