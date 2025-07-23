from fastapi import FastAPI
from scripts.ik_quaternion_combined import IKQuaternionCombiner
from Api.models import IKRequest, IKResponse
import rclpy

app = FastAPI()

# 初始化 ROS Node 和 IK 类，只初始化一次
rclpy.init()
ik_solver_node = IKQuaternionCombiner()

@app.post("/ik_solve", response_model=IKResponse)
def solve_ik(request: IKRequest):
    try:
        quat = ik_solver_node.build_quaternion(
            request.rotation.x_deg,
            request.rotation.y_deg,
            request.rotation.z_deg
        )

        success = ik_solver_node.calculate_ik(
            request.position.x,
            request.position.y,
            request.position.z,
            quat
        )

        if not success:
            return IKResponse(success=False, message="IK求解失败")

        return IKResponse(
            success=True,
            position=ik_solver_node.result_dict['position'],
            quaternion=ik_solver_node.result_dict['quaternion'],
            joints_deg=ik_solver_node.result_dict['joints_deg']
        )

    except Exception as e:
        return IKResponse(success=False, message=f"异常: {str(e)}")
