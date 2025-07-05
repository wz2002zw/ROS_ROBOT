import rclpy
from rclpy.node import Node
from moveit_msgs.action import MoveGroup
from geometry_msgs.msg import PoseStamped
from rclpy.action import ActionClient
import tf2_ros
from geometry_msgs.msg import TransformStamped

class MoveGroupClient(Node):
    def __init__(self):
        super().__init__('move_group_client')
        self._action_client = ActionClient(self, MoveGroup, 'move_action')
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

    def get_current_end_effector_pose(self):
        try:
            # 'base_link' -> 'Link6'，根据你的机器人调整末端链名称
            trans: TransformStamped = self.tf_buffer.lookup_transform(
                'base_link',
                'Link6',
                rclpy.time.Time()
            )
            self.get_logger().info(
                f"当前末端位姿: position=({trans.transform.translation.x:.3f}, "
                f"{trans.transform.translation.y:.3f}, {trans.transform.translation.z:.3f}), "
                f"orientation=({trans.transform.rotation.x:.3f}, {trans.transform.rotation.y:.3f}, "
                f"{trans.transform.rotation.z:.3f}, {trans.transform.rotation.w:.3f})"
            )
            return trans
        except Exception as e:
            self.get_logger().error(f"获取末端位姿失败: {e}")
            return None
    def send_goal(self, target_pose: PoseStamped):
        self.get_logger().info('Waiting for MoveGroup action server...')
        if not self._action_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('MoveGroup action server not available!')
            return

        goal_msg = MoveGroup.Goal()
        goal_msg.request.group_name = 'manipulator'   # ← 这里填上你的组名
        goal_msg.request.pipeline_id = 'ompl'         # 通常用 ompl
        # 设定工作空间边界（根据你的机械臂范围调整）
        goal_msg.request.workspace_parameters.header.frame_id = target_pose.header.frame_id
        goal_msg.request.workspace_parameters.min_corner.x = -1.0
        goal_msg.request.workspace_parameters.min_corner.y = -1.0
        goal_msg.request.workspace_parameters.min_corner.z = -1.0
        goal_msg.request.workspace_parameters.max_corner.x = 1.0
        goal_msg.request.workspace_parameters.max_corner.y = 1.0
        goal_msg.request.workspace_parameters.max_corner.z = 1.0

        # 允许基于当前状态做差异规划
        goal_msg.request.start_state.is_diff = True

        # 目标位姿约束，设置为机械臂末端位姿
        from moveit_msgs.msg import Constraints, PositionConstraint, OrientationConstraint
        from shape_msgs.msg import SolidPrimitive

        constraints = Constraints()
        # 位置约束
        pos_constraint = PositionConstraint()
        pos_constraint.header = target_pose.header
        pos_constraint.link_name = 'Link6'  # 替换为你的末端链名称
        pos_constraint.target_point_offset.x = 0.0
        pos_constraint.target_point_offset.y = 0.0
        pos_constraint.target_point_offset.z = 0.0
        sphere = SolidPrimitive()
        sphere.type = SolidPrimitive.SPHERE
        sphere.dimensions = [0.01]  # 允许位置误差半径
        pos_constraint.constraint_region.primitives = [sphere]
        pos_constraint.constraint_region.primitive_poses = [target_pose.pose]
        pos_constraint.weight = 1.0
        constraints.position_constraints.append(pos_constraint)

        # 姿态约束
        ori_constraint = OrientationConstraint()
        ori_constraint.header = target_pose.header
        ori_constraint.link_name = 'Link6'  # 替换为你的末端链名称
        ori_constraint.orientation = target_pose.pose.orientation
        ori_constraint.absolute_x_axis_tolerance = 0.1
        ori_constraint.absolute_y_axis_tolerance = 0.1
        ori_constraint.absolute_z_axis_tolerance = 0.1
        ori_constraint.weight = 1.0
        constraints.orientation_constraints.append(ori_constraint)

        goal_msg.request.goal_constraints.append(constraints)

        self.get_logger().info('Sending goal to MoveGroup...')
        send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected by MoveGroup action server')
            return
        self.get_logger().info('Goal accepted, waiting for result...')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info('Received feedback from MoveGroup')

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'MoveGroup result received. Error code: {result.error_code.val}')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = MoveGroupClient()
# 等待TF变换数据可用，循环等待最多5秒
    import time
    start_time = time.time()
    while rclpy.ok():
        try:
            current_pose = node.get_current_end_effector_pose()
            if current_pose is not None:
                break
        except Exception:
            pass
        rclpy.spin_once(node, timeout_sec=0.1)
        if time.time() - start_time > 5.0:
            node.get_logger().error("等待TF变换超时，退出")
            rclpy.shutdown()
            return

    if current_pose is None:
        node.get_logger().error("无法获取当前末端位姿，退出")
        rclpy.shutdown()
        return

    target_pose = PoseStamped()
    target_pose.header.frame_id = 'base_link'
    target_pose.header.stamp = node.get_clock().now().to_msg()
    target_pose.pose.position.x = -0.1
    target_pose.pose.position.y = 0.2
    target_pose.pose.position.z = 0.3
    target_pose.pose.orientation = current_pose.transform.rotation

    node.send_goal(target_pose)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
