import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

class MoveGroupJointClient(Node):
    def __init__(self):
        super().__init__('move_group_joint_client')
        self._action_client = ActionClient(self, FollowJointTrajectory, '/manipulator_controller/follow_joint_trajectory')
        self.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']

    def send_joint_goal(self, joint_positions):
        self.get_logger().info('等待动作服务器...')
        if not self._action_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('动作服务器未启动！')
            return False

        goal_msg = FollowJointTrajectory.Goal()
        goal_msg.trajectory.joint_names = self.joint_names

        point = JointTrajectoryPoint()
        point.positions = joint_positions
        point.time_from_start.sec = 2  # 2秒到达目标
        goal_msg.trajectory.points.append(point)

        self.get_logger().info(f'发送目标关节角度: {[round(p, 3) for p in joint_positions]}')
        send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        send_goal_future.add_done_callback(self.goal_response_callback)
        return True

    def feedback_callback(self, feedback_msg):
        self.get_logger().info('收到控制反馈...')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('目标被拒绝')
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
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = MoveGroupJointClient()

    # 这里写你想测试的关节角度
    target_joints = [0.7849, 2.5111, -2.3747, 1.5267, -0.6913, -2.2178]

    if node.send_joint_goal(target_joints):
        rclpy.spin(node)
    else:
        node.get_logger().error('无法发送目标')
        rclpy.shutdown()

if __name__ == '__main__':
    main()
