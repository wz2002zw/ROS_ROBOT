# Api/ik_Api.py
import rclpy
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import PoseStamped
from fastapi import FastAPI, HTTPException
from threading import Thread
import uvicorn

# 从 ik_node 中拿到真正的 ROS IK Client
from .ik_node import SimpleIKTester
from .models import PoseInput

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

    Thread(target=ros_spin, daemon=True).start()

@app.post("/ik")
def compute_ik(input_pose: PoseInput):
    if ros_node is None:
        raise HTTPException(status_code=500, detail="ROS node 未初始化")

    # 构造 MoveIt IK 服务需要的 PoseStamped
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

    # 调用 IK
    joints = ros_node.test_ik(pose)
    if joints is not None:
        return {"success": True, "joint_angles": joints}
    else:
        return {"success": False, "message": "IK求解失败"}

if __name__ == "__main__":
    uvicorn.run("ik_Api:app", host="0.0.0.0", port=8000)