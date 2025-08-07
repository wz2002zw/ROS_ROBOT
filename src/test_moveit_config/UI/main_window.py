from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QFrame, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from widgets.ik_widget import IKWidget  # 逆运动学模块
from widgets.simulation_controls import SimulationControls  # 仿真启动模块


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROS 机器人仿真控制系统")
        self.setGeometry(100, 100, 800, 600)  # 设置初始窗口大小
        self.init_ui()

    def init_ui(self):
        """初始化主窗口布局"""
        # 中心部件：承载所有内容
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)  # 外边框间距
        main_layout.setSpacing(15)  # 组件之间的间距

        # 1. 添加标题
        title_label = QLabel("机械臂逆运动学仿真系统")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # 2. 添加仿真启动控制模块（带边框）
        sim_frame = QFrame()
        sim_frame.setFrameShape(QFrame.Shape.StyledPanel)
        sim_frame.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        sim_layout = QHBoxLayout(sim_frame)
        sim_layout.addWidget(QLabel("仿真控制:"), alignment=Qt.AlignmentFlag.AlignLeft)
        self.sim_controls = SimulationControls()
        sim_layout.addWidget(self.sim_controls)
        main_layout.addWidget(sim_frame)

        # 3. 添加分隔线
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(line)

        # 4. 添加逆运动学计算模块（带边框）
        ik_frame = QFrame()
        ik_frame.setFrameShape(QFrame.Shape.StyledPanel)
        ik_frame.setStyleSheet("""
            QFrame {
                background-color: #f5f5f5;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        ik_layout = QVBoxLayout(ik_frame)
        ik_label = QLabel("逆运动学计算")
        ik_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        ik_layout.addWidget(ik_label)
        self.ik_widget = IKWidget()
        ik_layout.addWidget(self.ik_widget)
        main_layout.addWidget(ik_frame, stretch=1)  # 让IK模块占更多空间

        # 设置中心部件
        self.setCentralWidget(central_widget)