from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QFrame, QLabel, QScrollArea,
                             QTabWidget, QDialog, QApplication,
                             QMessageBox)
from PyQt6.QtCore import Qt, QSettings, QTimer, QPropertyAnimation, QEasingCurve, QUrl, QDateTime
from PyQt6.QtGui import QFont, QPixmap, QTextCursor, QMovie
from widgets.ik_widget import IKWidget
from widgets.quaternion_widget import QuaternionWidget
from widgets.simulation_controls import SimulationControls
from widgets.system_settings import SystemSettingsWidget  # 导入系统设置组件
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROS 机器人仿真控制系统")
        self.setGeometry(100, 100, 800, 700)
        
        # 初始化系统设置组件（包含启动动画逻辑）
        self.system_settings = SystemSettingsWidget()
        
        # 修复日志光标错误
        self.fix_log_cursor_errors()
        
        # 调用系统设置组件的方法显示启动动画（传入主窗口实例用于默认淡入）
        self.system_settings.show_startup_animation(parent_window=self)
        
        # 初始化UI并显示
        self.init_ui()
        self.show()

    def init_ui(self):
        """初始化主窗口布局"""
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # 标题
        title_label = QLabel("机械臂逆运动学与四元数仿真系统")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # 仿真控制模块
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

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(line)

        # 标签页
        tab_widget = QTabWidget()
        tab_widget.setFont(QFont("Arial", 10))

        # 四元数计算标签页
        quat_tab = QWidget()
        quat_tab_layout = QVBoxLayout(quat_tab)
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

        # 逆运动学标签页
        ik_tab = QWidget()
        ik_tab_layout = QVBoxLayout(ik_tab)
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

        # 系统设置标签页（直接使用已初始化的system_settings实例）
        settings_tab = QWidget()
        settings_tab_layout = QVBoxLayout(settings_tab)
        settings_scroll_area = QScrollArea()
        settings_scroll_area.setWidgetResizable(True)
        settings_scroll_area.setStyleSheet("QScrollArea { border: none; }")
        settings_scroll_area.setWidget(self.system_settings)  # 复用系统设置实例
        settings_tab_layout.addWidget(settings_scroll_area)
        tab_widget.addTab(settings_tab, "系统设置")

        main_layout.addWidget(tab_widget, stretch=1)
        self.setCentralWidget(central_widget)

    def fix_log_cursor_errors(self):
        """修复日志光标错误"""
        # 修复 quaternion_widget
        try:
            from widgets.quaternion_widget import QuaternionWidget
            
            def corrected_quat_append_log(self, text):
                current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
                self.log_display.append(f"[{current_time}] {text}")
                self.log_display.moveCursor(QTextCursor.MoveOperation.End)
            
            QuaternionWidget.append_log = corrected_quat_append_log
            print("已修复 quaternion_widget 的日志光标错误")
        except Exception as e:
            print(f"修复 quaternion_widget 失败: {str(e)}")

        # 修复 ik_widget
        try:
            from widgets.ik_widget import IKWidget
            
            def corrected_ik_append_log(self, message):
                current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
                self.log_display.append(f"[{current_time}] {message}")
                self.log_display.moveCursor(QTextCursor.MoveOperation.End)
            
            IKWidget.append_log = corrected_ik_append_log
            print("已修复 ik_widget 的日志光标错误")
        except Exception as e:
            print(f"修复 ik_widget 失败: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("ROS_Robot_UI")
    app.setOrganizationName("ROS_Robot")
    window = MainWindow()
    sys.exit(app.exec())