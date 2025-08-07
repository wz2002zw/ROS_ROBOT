import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from moveit_msgs.srv import GetPositionIK
import math

class IKSolver(Node):
    def __init__(self):
        super().__init__('ik_solver')
        self.cli = self.create_client(GetPositionIK, 'compute_ik')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待 compute_ik 服务...')

        self.group_name = 'manipulator'
        self.__target_joints = []  # 私有数组存储关节角度(角度制)

    @property
    def target_joints(self):
        """只读属性，允许外部访问但禁止修改"""
        return self.__target_joints.copy()  # 返回副本防止外部修改

    def solve_ik(self, pos, ori):
        """输入目标位置和四元数方向，返回角度解数组"""
        # 创建目标姿态对象
        pose = PoseStamped()
        pose.header.frame_id = 'base_link'
        pose.header.stamp = self.get_clock().now().to_msg()

        # 设置位置信息
        pose.pose.position.x = pos[0]
        pose.pose.position.y = pos[1]
        pose.pose.position.z = pos[2]

        # 设置姿态信息
        pose.pose.orientation.x = ori[0]
        pose.pose.orientation.y = ori[1]
        pose.pose.orientation.z = ori[2]
        pose.pose.orientation.w = ori[3]

        # 调用内部处理方法
        return self._process_ik_request(pose)

    def _process_ik_request(self, pose: PoseStamped):
        """处理IK求解请求的内部方法"""
        request = GetPositionIK.Request()
        request.ik_request.group_name = self.group_name
        request.ik_request.pose_stamped = pose
        request.ik_request.timeout.sec = 1

        future = self.cli.call_async(request)
        # rclpy.spin_until_future_complete(self, future)

        # 清空旧数据
        self.__target_joints.clear()

        if future.result() is not None:
            res = future.result()
            if res.error_code.val == 1:
                self.get_logger().info("IK求解成功，关节角度(角度制)：")
                for name, pos in zip(res.solution.joint_state.name, 
                                    res.solution.joint_state.position):
                    degree_pos = math.degrees(pos)  # 转换为角度制
                    self.__target_joints.append(degree_pos)
                    self.get_logger().info(f"  {name}: {degree_pos:.1f}°")
                return True, self.__target_joints
            else:
                self.get_logger().error(f"IK求解失败，错误码: {res.error_code.val}")
        else:
            self.get_logger().error("调用 compute_ik 服务失败")
            
        return False, []

def main(args=None):
    """测试函数"""
    rclpy.init(args=args)
    solver = IKSolver()
    
    # 测试位置和姿态
    test_pos = [0.2, 0.0, 0.5]
    test_ori = [0.0, 0.0, 0.0, 1.0]
    
    success, joints = solver.solve_ik(test_pos, test_ori)
    if success:
        print(f"求解成功，关节角度: {joints}")
    else:
        print("求解失败")
    
    solver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    