from PyQt6.QtWidgets import (QWidget, QFormLayout, QLineEdit, QPushButton, 
                             QTextEdit, QVBoxLayout, QHBoxLayout, QLabel,
                             QGroupBox)
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6 import QtGui
import sys
import os
import math  # 新增：用于计算等效旋转
from typing import Dict, Tuple, List

# 添加ROS包路径
ros_package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if ros_package_path not in sys.path:
    sys.path.append(ros_package_path)

# 直接导入你的四元数计算函数
from test_moveit_config.scripts.quaternion_mathematical_calculation import (
    calculate_quaternion,
    multiply_quaternions,
    normalize_quaternion,
    parse_input  # 复用输入解析函数（稍作适配）
)


class QuaternionThread(QThread):
    """处理四元数计算的后台线程，直接调用你的计算函数"""
    result_signal = pyqtSignal(bool, dict)  # (是否成功, 计算结果)
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.rotations = None  # 存储分离的旋转角度（x, y, z）
        self.running = True

    def run(self):
        try:
            self.log_signal.emit("四元数计算器初始化完成")
            
            while self.running:
                if self.rotations is not None:
                    try:
                        # 转换为原parse_input兼容的格式（"x 角度 y 角度 z 角度"）
                        user_input = f"x {self.rotations['x']} y {self.rotations['y']} z {self.rotations['z']}"
                        rotations = parse_input(user_input)
                        self.log_signal.emit(f"解析旋转序列: {rotations}")
                        
                        # 提取有效旋转
                        active_rotations = [(axis, angle) for axis, angle in rotations if abs(angle) > 1e-10]
                        
                        # 计算组合四元数（复用你的乘法函数）
                        combined_quaternion = (1.0, 0.0, 0.0, 0.0)
                        for axis, angle in rotations:
                            if abs(angle) > 1e-10:
                                current_q = calculate_quaternion(axis, angle)  # 调用你的函数
                                combined_quaternion = multiply_quaternions(current_q, combined_quaternion)  # 调用你的函数
                        
                        # 归一化（复用你的函数）
                        normalized_q = normalize_quaternion(combined_quaternion)
                        
                        # 计算等效旋转（复用原逻辑）
                        angle_radians = 2 * math.acos(normalized_q[0])
                        angle_degrees = math.degrees(angle_radians)
                        
                        if abs(angle_radians) < 1e-10:
                            axis_x, axis_y, axis_z = 1, 0, 0
                        else:
                            sin_half_angle = math.sin(angle_radians / 2)
                            axis_x = normalized_q[1] / sin_half_angle
                            axis_y = normalized_q[2] / sin_half_angle
                            axis_z = normalized_q[3] / sin_half_angle
                        
                        # 整理结果
                        result = {
                            "active_rotations": active_rotations,
                            "normalized_q": normalized_q,
                            "rotation_axis": (axis_x, axis_y, axis_z),
                            "rotation_angle": angle_degrees
                        }
                        
                        self.result_signal.emit(True, result)
                        
                    except SystemExit:
                        # 处理parse_input中可能的退出信号
                        self.log_signal.emit("用户请求退出计算")
                    except Exception as e:
                        self.log_signal.emit(f"计算错误: {str(e)}")
                        self.result_signal.emit(False, {"error": str(e)})
                    
                    finally:
                        self.rotations = None  # 重置计算请求
                
                self.msleep(100)  # 降低CPU占用

        except Exception as e:
            self.log_signal.emit(f"线程错误: {str(e)}")
        finally:
            self.log_signal.emit("四元数计算器已关闭")

    def calculate(self, rotations: Dict[str, float]):
        """接收分离的旋转角度（x, y, z）"""
        self.rotations = rotations
        self.log_signal.emit(f"收到计算请求: X={rotations['x']}°, Y={rotations['y']}°, Z={rotations['z']}°")

    def stop(self):
        """停止线程"""
        self.running = False
        self.wait()


class QuaternionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_calculation_thread()

    def init_ui(self):
        """初始化UI界面，X、Y、Z轴单独输入"""
        self.setWindowTitle("四元数计算")
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(12)  # 增加组件间距

        # 1. 旋转输入区域（X、Y、Z轴单独输入）
        input_group = QGroupBox("旋转角度设置（单位：度）")
        input_group.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Weight.Bold))
        input_layout = QFormLayout()
        
        # 单独的输入框
        self.x_input = QLineEdit("0.0")
        self.y_input = QLineEdit("0.0")
        self.z_input = QLineEdit("0.0")
        
        # 增加输入提示
        self.x_input.setPlaceholderText("输入绕X轴旋转角度")
        self.y_input.setPlaceholderText("输入绕Y轴旋转角度")
        self.z_input.setPlaceholderText("输入绕Z轴旋转角度")
        
        input_layout.addRow("X轴旋转:", self.x_input)
        input_layout.addRow("Y轴旋转:", self.y_input)
        input_layout.addRow("Z轴旋转:", self.z_input)
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        # 2. 按钮区域
        btn_layout = QHBoxLayout()
        self.calc_btn = QPushButton("计算四元数")
        self.clear_btn = QPushButton("重置")
        
        # 按钮样式优化
        self.calc_btn.setMinimumHeight(30)
        self.clear_btn.setMinimumHeight(30)
        
        self.calc_btn.clicked.connect(self.on_calculate)
        self.clear_btn.clicked.connect(self.on_clear)
        
        btn_layout.addWidget(self.calc_btn)
        btn_layout.addWidget(self.clear_btn)
        main_layout.addLayout(btn_layout)

        # 3. 结果显示区域
        result_group = QGroupBox("计算结果")
        result_group.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Weight.Bold))
        result_layout = QVBoxLayout()
        
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText("计算结果将显示在这里...")
        result_layout.addWidget(self.result_display)
        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)

        # 4. 状态与日志区域
        status_layout = QVBoxLayout()
        
        # 状态标签
        self.status_label = QLabel("状态: 就绪")
        self.status_label.setStyleSheet("color: blue; font-weight: bold;")
        
        # 日志区域
        log_group = QGroupBox("运行日志")
        log_group.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Weight.Bold))
        log_layout = QVBoxLayout()
        
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setMaximumHeight(100)
        log_layout.addWidget(self.log_display)
        log_group.setLayout(log_layout)
        
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(log_group)
        main_layout.addLayout(status_layout)

    def init_calculation_thread(self):
        """初始化计算线程"""
        self.calc_thread = QuaternionThread()
        self.calc_thread.result_signal.connect(self.handle_calculation_result)
        self.calc_thread.log_signal.connect(self.append_log)
        self.calc_thread.start()

    def get_rotation_input(self) -> Dict[str, float]:
        """获取X、Y、Z轴的旋转角度"""
        try:
            return {
                'x': float(self.x_input.text().strip()),
                'y': float(self.y_input.text().strip()),
                'z': float(self.z_input.text().strip())
            }
        except ValueError as e:
            self.append_log(f"输入错误: 请输入有效的数字（{str(e)}）")
            return None

    def on_calculate(self):
        """处理计算按钮点击事件"""
        self.status_label.setText("状态: 正在计算四元数...")
        self.status_label.setStyleSheet("color: orange; font-weight: bold;")
        
        rotations = self.get_rotation_input()
        if rotations:
            self.calc_thread.calculate(rotations)

    def handle_calculation_result(self, success: bool, result: dict):
        """处理计算结果"""
        if success:
            self.status_label.setText("状态: 计算成功")
            self.status_label.setStyleSheet("color: green; font-weight: bold;")
            
            # 格式化显示结果
            self.result_display.clear()
            
            # 显示旋转序列
            self.result_display.append("执行以下旋转：")
            for i, (axis, angle) in enumerate(result["active_rotations"], 1):
                self.result_display.append(f"  {i}. 绕 {axis.upper()} 轴旋转 {angle:.2f}°")
            
            # 显示四元数结果
            w, x, y, z = result["normalized_q"]
            self.result_display.append("\n组合后的四元数为：")
            self.result_display.append(f"  w = {w:.6f}")
            self.result_display.append(f"  x = {x:.6f}")
            self.result_display.append(f"  y = {y:.6f}")
            self.result_display.append(f"  z = {z:.6f}")
            self.result_display.append(f"  四元数形式：({w:.6f}, {x:.6f}i, {y:.6f}j, {z:.6f}k)")
            
            # 显示等效旋转
            axis = result["rotation_axis"]
            angle = result["rotation_angle"]
            self.result_display.append("\n等效的单一旋转：")
            self.result_display.append(f"  旋转轴: ({axis[0]:.6f}, {axis[1]:.6f}, {axis[2]:.6f})")
            self.result_display.append(f"  旋转角度: {angle:.6f}°")
            
        else:
            self.status_label.setText("状态: 计算失败")
            self.status_label.setStyleSheet("color: red; font-weight: bold;")
            self.result_display.setText(f"计算失败: {result.get('error', '未知错误')}")

    def append_log(self, message: str):
        """添加日志信息"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_display.append(f"[{timestamp}] {message}")
        self.log_display.moveCursor(self.log_display.textCursor().End)

    def on_clear(self):
        """清空输入和结果"""
        self.x_input.setText("0.0")
        self.y_input.setText("0.0")
        self.z_input.setText("0.0")
        
        self.result_display.clear()
        self.status_label.setText("状态: 就绪")
        self.status_label.setStyleSheet("color: blue; font-weight: bold;")
        self.append_log("已重置输入和结果")

    def closeEvent(self, event):
        """窗口关闭时清理资源"""
        self.calc_thread.stop()
        event.accept()