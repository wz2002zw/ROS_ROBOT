import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from moveit_msgs.srv import GetPositionIK
import math

class SimpleIKTester(Node):
    def __init__(self):
        super().__init__('simple_ik_tester')

        self.cli = self.create_client(GetPositionIK, 'compute_ik')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待 compute_ik 服务...')

        self.group_name = 'manipulator'

    def test_ik(self, pose: PoseStamped):
        request = GetPositionIK.Request()
        request.ik_request.group_name = self.group_name
        request.ik_request.pose_stamped = pose
        request.ik_request.timeout.sec = 1

        future = self.cli.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            res = future.result()
            if res.error_code.val == 1:
                self.get_logger().info("IK求解成功，关节角度(弧度)：")
                for name, pos in zip(res.solution.joint_state.name, res.solution.joint_state.position):
                    self.get_logger().info(f"  {name}: {pos:.4f} ({math.degrees(pos):.1f}°)")
            else:
                self.get_logger().error(f"IK求解失败，错误码: {res.error_code.val}")
        else:
            self.get_logger().error("调用 compute_ik 服务失败")

def main(args=None):
    rclpy.init(args=args)
    node = SimpleIKTester()

    target_pose = PoseStamped()
    target_pose.header.frame_id = 'base_link'
    target_pose.header.stamp = node.get_clock().now().to_msg()
    target_pose.pose.position.x = 0.2
    target_pose.pose.position.y = 0.0
    target_pose.pose.position.z = 0.5
    target_pose.pose.orientation.x = 0.0
    target_pose.pose.orientation.y = 0.0
    target_pose.pose.orientation.z = 0.0
    target_pose.pose.orientation.w = 1.0

    node.test_ik(target_pose)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
