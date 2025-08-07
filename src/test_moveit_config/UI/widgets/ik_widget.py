from PyQt6.QtWidgets import (QWidget, QFormLayout, QLineEdit, QPushButton, 
                             QTextEdit, QVBoxLayout, QHBoxLayout, QLabel)
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from geometry_msgs.msg import PoseStamped
import rclpy
import math
import sys
import os

# 添加ROS包路径到Python搜索路径
ros_package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if ros_package_path not in sys.path:
    sys.path.append(ros_package_path)

# 只导入逆运动学核心模块（不依赖运动控制模块）
from test_moveit_config.scripts.ik_mathematical_calculation_safe import SimpleIKTester


class ROSIKThread(QThread):
    """仅处理逆运动学计算的ROS线程"""
    result_signal = pyqtSignal(bool, list)  # (是否成功, 关节角度列表)
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ik_tester = None
        self.pose = None
        self.running = True

    def run(self):
        try:
            rclpy.init(args=None)
            self.ik_tester = SimpleIKTester()
            self.log_signal.emit("逆运动学求解器初始化完成，等待计算指令...")
            
            while self.running and rclpy.ok():
                if self.pose is not None:
                    # 仅调用逆运动学计算（不涉及运动执行）
                    success = self.ik_tester.test_ik(self.pose)
                    joint_angles = self.ik_tester.target_joints if success else []
                    self.result_signal.emit(success, joint_angles)
                    self.pose = None  # 重置计算请求
                rclpy.spin_once(self.ik_tester, timeout_sec=0.1)  # 非阻塞处理ROS事件

        except Exception as e:
            self.log_signal.emit(f"逆运动学线程错误: {str(e)}")
        finally:
            if rclpy.ok():
                rclpy.shutdown()
            self.log_signal.emit("逆运动学求解器已关闭")

    def calculate_ik(self, pose: PoseStamped):
        """接收UI线程的计算请求"""
        self.pose = pose
        self.log_signal.emit("开始计算逆运动学...")

    def stop(self):
        """停止线程"""
        self.running = False
        self.wait()


class IKWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.joint_angles = []  # 存储计算得到的关节角度
        self.init_ui()
        self.init_ros_threads()  # 初始化逆运动学计算线程

    def init_ui(self):
        """初始化UI界面（移除运动执行相关组件）"""
        self.setWindowTitle("逆运动学计算")
        main_layout = QVBoxLayout(self)

        # 1. 坐标输入区域（保持不变）
        input_layout = QFormLayout()
        self.x_input = QLineEdit("0.2")
        self.y_input = QLineEdit("0.0")
        self.z_input = QLineEdit("0.5")
        self.ox_input = QLineEdit("0.0")
        self.oy_input = QLineEdit("0.0")
        self.oz_input = QLineEdit("0.0")
        self.ow_input = QLineEdit("1.0")

        input_layout.addRow("X坐标 (m):", self.x_input)
        input_layout.addRow("Y坐标 (m):", self.y_input)
        input_layout.addRow("Z坐标 (m):", self.z_input)
        input_layout.addRow("姿态X (ox):", self.ox_input)
        input_layout.addRow("姿态Y (oy):", self.oy_input)
        input_layout.addRow("姿态Z (oz):", self.oz_input)
        input_layout.addRow("姿态W (ow):", self.ow_input)

        # 2. 按钮区域（移除"执行运动"按钮）
        btn_layout = QHBoxLayout()
        self.calc_btn = QPushButton("计算逆运动学")
        self.clear_btn = QPushButton("清空")
        self.calc_btn.clicked.connect(self.on_calculate)
        self.clear_btn.clicked.connect(self.on_clear)
        btn_layout.addWidget(self.calc_btn)
        btn_layout.addWidget(self.clear_btn)

        # 3. 结果显示区域（保持不变）
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText("计算结果将显示在这里...")

        # 4. 状态与日志区域（简化状态描述）
        status_layout = QVBoxLayout()
        self.status_label = QLabel("状态: 就绪")
        self.status_label.setStyleSheet("color: blue; font-weight: bold;")
        
        log_label = QLabel("运行日志:")
        log_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setMaximumHeight(120)
        
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(log_label)
        status_layout.addWidget(self.log_display)

        # 组装布局
        main_layout.addLayout(input_layout)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(QLabel("关节角度结果 (角度制):"))
        main_layout.addWidget(self.result_display)
        main_layout.addLayout(status_layout)

    def init_ros_threads(self):
        """仅初始化逆运动学计算线程"""
        self.ik_thread = ROSIKThread()
        self.ik_thread.result_signal.connect(self.handle_ik_result)
        self.ik_thread.log_signal.connect(self.append_log)
        self.ik_thread.start()

    def get_pose_from_input(self):
        """从输入框获取位姿信息并转换为PoseStamped"""
        try:
            x = float(self.x_input.text())
            y = float(self.y_input.text())
            z = float(self.z_input.text())
            ox = float(self.ox_input.text())
            oy = float(self.oy_input.text())
            oz = float(self.oz_input.text())
            ow = float(self.ow_input.text())

            pose = PoseStamped()
            pose.header.frame_id = "base_link"
            pose.header.stamp = rclpy.clock.Clock().now().to_msg()
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.position.z = z
            pose.pose.orientation.x = ox
            pose.pose.orientation.y = oy
            pose.pose.orientation.z = oz
            pose.pose.orientation.w = ow
            return pose
            
        except ValueError as e:
            self.append_log(f"输入错误: 请输入有效的数字（{str(e)}）")
            return None

    def on_calculate(self):
        """处理计算按钮点击事件"""
        self.status_label.setText("状态: 正在计算逆运动学...")
        self.status_label.setStyleSheet("color: orange; font-weight: bold;")
        
        pose = self.get_pose_from_input()
        if pose:
            self.ik_thread.calculate_ik(pose)

    def handle_ik_result(self, success: bool, joint_angles: list):
        """处理逆运动学计算结果"""
        if success:
            self.joint_angles = joint_angles
            self.result_display.clear()
            for i, angle in enumerate(joint_angles, 1):
                self.result_display.append(f"关节J{i}: {angle:.2f}°")
            
            self.status_label.setText("状态: 逆运动学计算成功")
            self.status_label.setStyleSheet("color: green; font-weight: bold;")
            self.append_log(f"逆运动学求解成功，共{len(joint_angles)}个关节角度")
        else:
            self.joint_angles = []
            self.result_display.setText("求解失败，请检查目标位姿是否可达")
            self.status_label.setText("状态: 逆运动学计算失败")
            self.status_label.setStyleSheet("color: red; font-weight: bold;")

    def append_log(self, message: str):
        """添加带时间戳的日志信息"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_display.append(f"[{timestamp}] {message}")
        self.log_display.moveCursor(self.log_display.textCursor().End)

    def on_clear(self):
        """清空输入和结果"""
        self.x_input.setText("0.2")
        self.y_input.setText("0.0")
        self.z_input.setText("0.5")
        self.ox_input.setText("0.0")
        self.oy_input.setText("0.0")
        self.oz_input.setText("0.0")
        self.ow_input.setText("1.0")
        
        self.result_display.clear()
        self.joint_angles = []
        self.status_label.setText("状态: 就绪")
        self.status_label.setStyleSheet("color: blue; font-weight: bold;")
        self.append_log("已清空输入和结果")

    def closeEvent(self, event):
        """窗口关闭时停止ROS线程"""
        self.ik_thread.stop()
        event.accept()