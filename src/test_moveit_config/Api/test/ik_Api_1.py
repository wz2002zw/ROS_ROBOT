# ik_Api.py
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import PoseStamped
from moveit_msgs.srv import GetPositionIK
import math
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from threading import Thread
import uvicorn

# -------- ROS 节点封装 --------
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

        # 使用异步 future，不使用 spin_until_future_complete
        future = self.cli.call_async(request)
        while not future.done():
            rclpy.spin_once(self, timeout_sec=0.1)

        if future.result() and future.result().error_code.val == 1:
            joint_angles = [math.degrees(p) for p in future.result().solution.joint_state.position]
            return joint_angles
        return None

# -------- FastAPI 定义 --------
class Position(BaseModel):
    x: float
    y: float
    z: float

class Orientation(BaseModel):
    x: float
    y: float
    z: float
    w: float
    
class PoseInput(BaseModel):
    position: Position
    orientation: Orientation

app = FastAPI()
ros_node: SimpleIKTester = None

@app.on_event("startup")
def ros2_start():
    def ros_spin():
        global ros_node
        rclpy.init()
        ros_node = SimpleIKTester()
        executor = MultiThreadedExecutor()
        executor.add_node(ros_node)
        executor.spin()

    thread = Thread(target=ros_spin, daemon=True)
    thread.start()

@app.post("/ik")
def compute_ik(input_pose: PoseInput):
    if ros_node is None:
        raise HTTPException(status_code=500, detail="ROS node 未初始化")

    pose = PoseStamped()
    pose.header.frame_id = 'base_link'
    pose.header.stamp = ros_node.get_clock().now().to_msg()
    pose.pose.position.x = input_pose.position.x
    pose.pose.position.y = input_pose.position.y
    pose.pose.position.z = input_pose.position.z
    pose.pose.orientation.x = input_pose.orientation.x
    pose.pose.orientation.y = input_pose.orientation.y
    pose.pose.orientation.z = input_pose.orientation.z
    pose.pose.orientation.w = input_pose.orientation.w

    result = ros_node.test_ik(pose)
    if result is not None:
        return {"success": True, "joint_angles": result}
    else:
        return {"success": False, "message": "IK求解失败"}

if __name__ == "__main__":
    uvicorn.run("ik_Api:app", host="0.0.0.0", port=8000)
