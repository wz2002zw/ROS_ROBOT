import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from moveit_msgs.srv import GetPositionIK
import math
import sys
import os

# 添加脚本路径，导入已有的四元数和IK模块
sys.path.append('/home/wz/Desktop/ROS_ROBOT/src/test_moveit_config/scripts')
from quaternion_mathematical_calculation import calculate_quaternion, multiply_quaternions, normalize_quaternion

class IKQuaternionCombiner(Node):
    def __init__(self):
        super().__init__('ik_quaternion_combiner')
        self.cli = self.create_client(GetPositionIK, 'compute_ik')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待 compute_ik 服务...')
        self.group_name = 'manipulator'
        self.result_dict = {}

    def build_quaternion(self, x_deg, y_deg, z_deg):
        qx = calculate_quaternion('x', x_deg)
        qy = calculate_quaternion('y', y_deg)
        qz = calculate_quaternion('z', z_deg)
        q_combined = multiply_quaternions(qz, multiply_quaternions(qy, qx))
        return normalize_quaternion(q_combined)

    def calculate_ik(self, x, y, z, q):
        pose = PoseStamped()
        pose.header.frame_id = 'base_link'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z
        pose.pose.orientation.w = q[0]
        pose.pose.orientation.x = q[1]
        pose.pose.orientation.y = q[2]
        pose.pose.orientation.z = q[3]

        request = GetPositionIK.Request()
        request.ik_request.group_name = self.group_name
        request.ik_request.pose_stamped = pose
        request.ik_request.timeout.sec = 2

        future = self.cli.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            res = future.result()
            if res.error_code.val == 1:
                joint_angles_deg = [math.degrees(p) for p in res.solution.joint_state.position]
                joint_names = res.solution.joint_state.name

                self.get_logger().info("IK 求解成功:")
                for name, angle in zip(joint_names, joint_angles_deg):
                    self.get_logger().info(f"  {name}: {angle:.1f}°")

                self.result_dict = {
                    'position': (x, y, z),
                    'quaternion': q,
                    'joints_deg': dict(zip(joint_names, joint_angles_deg))
                }
                return True
            else:
                self.get_logger().error(f"IK求解失败，错误码: {res.error_code.val}")
        else:
            self.get_logger().error("调用 compute_ik 服务失败")
        return False

# ✅ 新增函数：供 API 或其他脚本调用
def run_ik_solver(x, y, z, x_deg, y_deg, z_deg):
    rclpy.init()
    node = IKQuaternionCombiner()
    try:
        quat = node.build_quaternion(x_deg, y_deg, z_deg)
        success = node.calculate_ik(x, y, z, quat)
        result = node.result_dict if success else {"error": "IK 求解失败"}
    except Exception as e:
        result = {"error": str(e)}
    finally:
        node.destroy_node()
        rclpy.shutdown()
    return result

# ✅ 原本命令行交互保留
def main(args=None):
    rclpy.init(args=args)
    node = IKQuaternionCombiner()

    print("\n==== 输入位姿信息进行IK与姿态计算 ====")
    try:
        pos_input = input("请输入末端位置 (x y z)，单位米：")
        x, y, z = map(float, pos_input.strip().split())

        rot_input = input("请输入绕 x y z 的旋转角度 (单位°)，例如: 90 0 45：")
        x_deg, y_deg, z_deg = map(float, rot_input.strip().split())

        quat = node.build_quaternion(x_deg, y_deg, z_deg)

        print(f"\n生成四元数：w={quat[0]:.4f}, x={quat[1]:.4f}, y={quat[2]:.4f}, z={quat[3]:.4f}")

        if node.calculate_ik(x, y, z, quat):
            print("\n== 综合结果 ==")
            print(f"位置: {node.result_dict['position']}")
            print(f"四元数: {node.result_dict['quaternion']}")
            print(f"关节角度 (角度制):")
            for name, angle in node.result_dict['joints_deg'].items():
                print(f"  {name}: {angle:.1f}°")

    except Exception as e:
        print(f"发生错误：{e}")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
