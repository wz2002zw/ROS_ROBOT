import socket
import json
import time
from typing import List, Optional
import rclpy  # 引入ROS2 Python客户端库
from geometry_msgs.msg import PoseStamped
from ik_mathematical_calculation_safe import SimpleIKTester  # 导入逆运动学模块

SERVER_IP = '10.168.1.38'
SERVER_PORT = 5005

def create_json_frame(
    pack_id: str,
    m_values: Optional[List[float]] = None,
    **kwargs
) -> str:
    """创建JSON帧，直接使用角度制关节角度"""
    # 初始化8个参数为0
    full_m_values = [0.0] * 8
    
    # 用提供的参数更新默认值（直接使用角度制）
    if m_values:
        for i, value in enumerate(m_values):
            if i < 8:  # 确保不超出范围
                full_m_values[i] = value  # 直接使用角度值，不做转换
    
    payload = {
        "dsID": "www.hc-system.com.HCRemoteCommand",
        "reqType": "AddRCC",
        "emptyList": "1",
        "packID": pack_id,
        "instructions": [{
            "oneshot": "0",
            "action": "4",
            "m0": full_m_values[0],  # 直接使用数值，不转换为字符串
            "m1": full_m_values[1],
            "m2": full_m_values[2],
            "m3": full_m_values[3],
            "m4": full_m_values[4],
            "m5": full_m_values[5],
            "m6": full_m_values[6],
            "m7": full_m_values[7],
            "ckStatus": "0xFF",
            "speed": "80.0",
            "delay": "1.0",
            "coord": "0",
            "tool": "0",
            "smooth": "0"
        }]
    }
    
    # 允许覆盖其他参数
    payload['instructions'][0].update(kwargs)
    
    return json.dumps(payload, ensure_ascii=False)

def calculate_ik_angles(target_pose: PoseStamped) -> Optional[List[float]]:
    """计算逆运动学并返回关节角度（角度制）"""
    rclpy.init(args=None)
    try:
        node = SimpleIKTester()
        if node.test_ik(target_pose):
            angles = node.target_joints
            node.destroy_node()
            return angles
        else:
            node.destroy_node()
            return None
    finally:
        rclpy.shutdown()

def send_json_frames():
    """发送JSON帧的主函数"""
    # 定义多个目标位姿
    target_poses = [
        PoseStamped(),  # 默认位姿
        PoseStamped(),  # 其他位姿
        PoseStamped(),  # 更多位姿
    ]
    
    # 设置不同的目标位置
    target_poses[0].header.frame_id = 'base_link'
    target_poses[0].pose.position.x = 0.2
    target_poses[0].pose.position.y = 0.0
    target_poses[0].pose.position.z = 0.5
    target_poses[0].pose.orientation.x = 0.0
    target_poses[0].pose.orientation.y = 0.0
    target_poses[0].pose.orientation.z = 0.0
    target_poses[0].pose.orientation.w = 1.0
    
    # 设置其他位姿...
    target_poses[1].header.frame_id = 'base_link'
    target_poses[1].pose.position.x = 0.3
    target_poses[1].pose.position.y = 0.1
    target_poses[1].pose.position.z = 0.6
    
    target_poses[2].header.frame_id = 'base_link'
    target_poses[2].pose.position.x = 0.25
    target_poses[2].pose.position.y = -0.1
    target_poses[2].pose.position.z = 0.55
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.settimeout(10)
            client_socket.connect((SERVER_IP, SERVER_PORT))
            print(f"成功连接到服务器 {SERVER_IP}:{SERVER_PORT}")
            
            frame_count = 0
            while True:
                pose_index = frame_count % len(target_poses)
                current_pose = target_poses[pose_index]
                
                print(f"计算位姿 {pose_index} 的逆运动学...")
                joint_angles = calculate_ik_angles(current_pose)
                
                if joint_angles:
                    print(f"获取关节角度(角度制): {joint_angles}")
                    
                    # 直接使用角度制关节角度（无需转换为弧度）
                    m_values = joint_angles[:8]  # 取前8个关节角度
                    
                    message = create_json_frame(
                        pack_id=str(frame_count),
                        m_values=m_values,
                        speed="50.0" if frame_count % 2 == 0 else "80.0"
                    )
                    
                    client_socket.sendall(message.encode('utf-8'))
                    print(f"已发送帧 #{frame_count} (位姿 {pose_index}): {message}")
                    
                    try:
                        response = client_socket.recv(1024)
                        if response:
                            print(f"收到响应: {response.decode('utf-8')}")
                    except socket.timeout:
                        print("接收超时，继续发送下一帧")
                else:
                    print(f"位姿 {pose_index} 的逆运动学计算失败，跳过此帧")
                
                frame_count += 1
                time.sleep(1)
                
        except socket.error as se:
            print(f"Socket错误: {se}")
        except KeyboardInterrupt:
            print("\n程序被用户中断")
        except Exception as e:
            print(f"发生未知错误: {e}")
        finally:
            print("连接已关闭")

if __name__ == "__main__":
    send_json_frames()