import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from ik_mathematical_calculation_safe import SimpleIKTester  # 导入逆运动学模块
from geometry_msgs.msg import PoseStamped
import math

class MoveGroupJointClient(Node):
    def __init__(self):
        super().__init__('move_group_joint_client')
        self._action_client = ActionClient(self, FollowJointTrajectory, '/manipulator_controller/follow_joint_trajectory')
        self.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        
        # 初始化逆运动学计算器
        self.ik_tester = SimpleIKTester()
        self.get_logger().info('路径规划节点初始化完成')
        
        # 标记ROS上下文是否已关闭
        self.context_shutdown = False

    def plan_and_execute(self, target_pose: PoseStamped):
        """规划路径并执行"""
        self.get_logger().info('开始路径规划...')
        
        # 调用逆运动学计算
        if self.ik_tester.test_ik(target_pose):
            joint_angles = self.ik_tester.target_joints  # 获取计算结果（角度制）
            self.get_logger().info(f"获取关节角度(角度制): {joint_angles}")
            
            # 发送关节角度目标
            return self.send_joint_goal(joint_angles)
        else:
            self.get_logger().error('逆运动学计算失败')
            return False

    def send_joint_goal(self, joint_positions):
        """发送关节角度目标到机械臂控制器"""
        self.get_logger().info('等待动作服务器...')
        if not self._action_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('动作服务器未启动！')
            return False

        goal_msg = FollowJointTrajectory.Goal()
        goal_msg.trajectory.joint_names = self.joint_names

        point = JointTrajectoryPoint()
        # 将角度制转换为弧度制
        radian_positions = [math.radians(p) for p in joint_positions]
        point.positions = radian_positions
        point.time_from_start.sec = 3  # 3秒到达目标
        goal_msg.trajectory.points.append(point)

        self.get_logger().info(f'发送目标关节角度(弧度): {[round(p, 3) for p in radian_positions]}')
        send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        send_goal_future.add_done_callback(self.goal_response_callback)
        return True

    def feedback_callback(self, feedback_msg):
        # 减少反馈日志输出频率，避免刷屏
        if int(self.get_clock().now().nanoseconds * 1e-9) % 5 == 0:
            self.get_logger().info('收到控制反馈...')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('目标被拒绝')
            self._shutdown()
            return
        self.get_logger().info('目标被接受，等待结果...')
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        if result.error_code == 0:
            self.get_logger().info('轨迹执行成功！')
        else:
            self.get_logger().error(f'轨迹执行失败，错误码: {result.error_code}')
        self._shutdown()

    def _shutdown(self):
        """安全关闭ROS上下文的辅助方法"""
        if not self.context_shutdown:
            self.context_shutdown = True
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = MoveGroupJointClient()

    try:
        # 定义目标位姿
        target_pose = PoseStamped()
        target_pose.header.frame_id = 'base_link'
        target_pose.header.stamp = node.get_clock().now().to_msg()
        target_pose.pose.position.x = 0.3  # 目标位置
        target_pose.pose.position.y = 0.1
        target_pose.pose.position.z = 0.6
        target_pose.pose.orientation.x = 0.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 1.0

        # 规划并执行
        node.get_logger().info('开始规划并执行...')
        if node.plan_and_execute(target_pose):
            rclpy.spin(node)
        else:
            node.get_logger().error('路径规划或执行失败')
            node._shutdown()
    
    except KeyboardInterrupt:
        node.get_logger().info('用户中断程序')
        node._shutdown()
    finally:
        # 不再需要在这里调用rclpy.shutdown()，因为已经在动作回调中处理
        node.destroy_node()

if __name__ == '__main__':
    main()