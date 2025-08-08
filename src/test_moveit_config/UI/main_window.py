from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QFrame, QLabel, QScrollArea,
                             QTabWidget)  # 新增QTabWidget用于标签页
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from widgets.ik_widget import IKWidget  # 逆运动学模块
from widgets.quaternion_widget import QuaternionWidget  # 四元数计算模块
from widgets.simulation_controls import SimulationControls  # 仿真启动模块


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROS 机器人仿真控制系统")
        self.setGeometry(100, 100, 800, 700)  # 适当增大窗口
        self.init_ui()

    def init_ui(self):
        """初始化主窗口布局，添加标签页组织不同功能"""
        # 中心部件：承载所有内容
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # 1. 添加标题
        title_label = QLabel("机械臂逆运动学与四元数仿真系统")
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

        # 4. 使用标签页组织不同功能模块
        tab_widget = QTabWidget()
        tab_widget.setFont(QFont("Arial", 10))

        # 4.1 逆运动学标签页
        ik_tab = QWidget()
        ik_tab_layout = QVBoxLayout(ik_tab)
        
        # 为逆运动学模块添加滚动区域
        ik_scroll_area = QScrollArea()
        ik_scroll_area.setWidgetResizable(True)
        ik_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        ik_scroll_area.setStyleSheet("QScrollArea { border: none; }")
        
        ik_container = QWidget()
        ik_container_layout = QVBoxLayout(ik_container)
        self.ik_widget = IKWidget()
        ik_container_layout.addWidget(self.ik_widget)
        ik_scroll_area.setWidget(ik_container)
        
        ik_tab_layout.addWidget(ik_scroll_area)
        tab_widget.addTab(ik_tab, "逆运动学计算")

        # 4.2 四元数计算标签页
        quat_tab = QWidget()
        quat_tab_layout = QVBoxLayout(quat_tab)
        
        # 为四元数模块添加滚动区域
        quat_scroll_area = QScrollArea()
        quat_scroll_area.setWidgetResizable(True)
        quat_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        quat_scroll_area.setStyleSheet("QScrollArea { border: none; }")
        
        quat_container = QWidget()
        quat_container_layout = QVBoxLayout(quat_container)
        self.quaternion_widget = QuaternionWidget()
        quat_container_layout.addWidget(self.quaternion_widget)
        quat_scroll_area.setWidget(quat_container)
        
        quat_tab_layout.addWidget(quat_scroll_area)
        tab_widget.addTab(quat_tab, "四元数计算")

        # 添加标签页到主布局
        main_layout.addWidget(tab_widget, stretch=1)

        # 设置中心部件
        self.setCentralWidget(central_widget)
