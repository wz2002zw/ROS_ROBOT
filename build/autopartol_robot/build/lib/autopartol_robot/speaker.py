import rclpy
from rclpy.node import Node
from autopartol_interfaces.srv import SpeechText
import subprocess  # 用于调用 espeak

class Speaker(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.speech_service = self.create_service(SpeechText, 'speech_text', self.speech_text_callback)

    def speech_text_callback(self, request, response):
        self.get_logger().info(f'正在准备朗读 {request.text}')
        
        # **使用 subprocess 直接调用 espeak**
        subprocess.run(["espeak", "-v", "zh", request.text], check=True)
        
        response.result = True
        return response

def main():
    rclpy.init()
    node = Speaker('speaker')
    rclpy.spin(node)
    rclpy.shutdown()
