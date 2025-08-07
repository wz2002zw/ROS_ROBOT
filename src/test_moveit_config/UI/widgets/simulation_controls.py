from PyQt6.QtWidgets import QFrame, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QFont
import subprocess
import os

class SimulationControls(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 去除内边距

        # 美化按钮样式
        self.start_sim_button = QPushButton("启动仿真")
        self.start_sim_button.setFont(QFont("Arial", 10))
        self.start_sim_button.setMinimumHeight(30)
        self.start_sim_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.start_sim_button.clicked.connect(self.launch_simulation)

        layout.addWidget(self.start_sim_button)
        self.setLayout(layout)

    def launch_simulation(self):
        try:
            # 启动ROS2仿真的命令（保持不变）
            launch_cmd = [
                "gnome-terminal", "--", "bash", "-c",
                "source /opt/ros/humble/setup.bash && "
                "source ~/Desktop/ROS_ROBOT/install/setup.bash && "
                "ros2 launch test_moveit_config demo.launch.py; exec bash"
            ]
            subprocess.Popen(launch_cmd)
            QMessageBox.information(self, "启动成功", "仿真已启动，正在打开终端...")
        except Exception as e:
            QMessageBox.critical(self, "启动失败", f"启动仿真失败: {str(e)}")