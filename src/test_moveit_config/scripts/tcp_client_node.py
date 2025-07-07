import socket
import json
import time
from typing import List, Optional

SERVER_IP = '10.168.1.38'
SERVER_PORT = 5005

def create_json_frame(
    pack_id: str,
    m_values: Optional[List[float]] = None,
    **kwargs
) -> str:
    """
    创建JSON帧，支持部分参数输入，未提供的参数自动补零
    
    Args:
        pack_id: 消息包ID
        m_values: 包含m0-m7参数值的数组，长度可以小于8，未提供的参数将补零
        **kwargs: 其他可覆盖的指令参数
    """
    # 初始化8个参数为0
    full_m_values = [0.0] * 8
    
    # 用提供的参数更新默认值
    if m_values:
        for i, value in enumerate(m_values):
            if i < 8:  # 确保不超出范围
                full_m_values[i] = value
    
    payload = {
        "dsID": "www.hc-system.com.HCRemoteCommand",
        "reqType": "AddRCC",
        "emptyList": "1",
        "packID": pack_id,
        "instructions": [{
            "oneshot": "0",
            "action": "4",
            "m0": f"{full_m_values[0]:.3f}",
            "m1": f"{full_m_values[1]:.3f}",
            "m2": f"{full_m_values[2]:.3f}",
            "m3": f"{full_m_values[3]:.3f}",
            "m4": f"{full_m_values[4]:.3f}",
            "m5": f"{full_m_values[5]:.3f}",
            "m6": f"{full_m_values[6]:.3f}",
            "m7": f"{full_m_values[7]:.3f}",
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

def send_json_frames():
    """发送JSON帧的主函数"""
    parameter_sets = [
        [],                      # 全部使用默认值(全零)
        [10.5, -5.2],           # 只设置m0和m1
        [0.0, 0.0, 0.0, 0.0, -45.0],  # 只设置前5个参数
        [0.0, 0.0, 0.0, 0.0, -90.0, 0.0, 0.0, 0.0],  # 完整设置
        [5.0, 5.0, 5.0, 5.0, -90.0, 30.0, 45.0],  # 前7个参数
    ]
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.settimeout(10)
            client_socket.connect((SERVER_IP, SERVER_PORT))
            print(f"成功连接到服务器 {SERVER_IP}:{SERVER_PORT}")
            
            frame_count = 0
            while True:
                param_index = frame_count % len(parameter_sets)
                current_params = parameter_sets[param_index]
                
                message = create_json_frame(
                    pack_id=str(frame_count),
                    m_values=current_params,
                    speed="50.0" if param_index % 2 == 0 else "80.0"  # 示例: 动态修改其他参数
                )
                
                client_socket.sendall(message.encode('utf-8'))
                print(f"已发送帧 #{frame_count} (参数集 {param_index}): {message}")
                
                try:
                    response = client_socket.recv(1024)
                    if response:
                        print(f"收到响应: {response.decode('utf-8')}")
                except socket.timeout:
                    print("接收超时，继续发送下一帧")
                
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