from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QCheckBox, QLineEdit, 
                             QPushButton, QFrame, QFileDialog)
from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QFont

class SystemSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("RobotSim", "ROSController")  # 用于保存配置
        self.init_ui()
        self.load_settings()  # 加载保存的设置

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # 标题
        title_label = QLabel("系统设置")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)
        
        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)
        
        # 页面动画设置
        anim_layout = QHBoxLayout()
        anim_label = QLabel("启用页面启动动画:")
        self.anim_checkbox = QCheckBox()
        anim_layout.addWidget(anim_label)
        anim_layout.addWidget(self.anim_checkbox)
        anim_layout.addStretch()
        layout.addLayout(anim_layout)
        
        # 视频动画设置
        video_frame = QFrame()
        video_frame.setFrameShape(QFrame.Shape.StyledPanel)
        video_frame.setStyleSheet("""
            QFrame {
                background-color: #f5f5f5;
                border-radius: 4px;
                padding: 10px;
            }
        """)
        video_layout = QVBoxLayout(video_frame)
        
        video_title = QLabel("启动视频动画设置")
        video_title.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        video_layout.addWidget(video_title)
        
        # 视频路径输入
        path_layout = QHBoxLayout()
        path_label = QLabel("视频文件路径:")
        self.video_path_edit = QLineEdit()
        self.video_path_edit.setPlaceholderText("请输入视频文件路径或点击浏览选择")
        browse_btn = QPushButton("浏览...")
        browse_btn.clicked.connect(self.browse_video_file)
        
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.video_path_edit, 1)
        path_layout.addWidget(browse_btn)
        video_layout.addLayout(path_layout)
        
        # 应用按钮
        self.apply_video_btn = QPushButton("设置为启动动画")
        self.apply_video_btn.clicked.connect(self.save_video_settings)
        video_layout.addWidget(self.apply_video_btn, alignment=Qt.AlignmentFlag.AlignRight)
        
        layout.addWidget(video_frame)
        
        # 说明文字
        note_label = QLabel("""<small><b>说明:</b><br>
        1. 支持的视频格式: MP4, AVI, MOV<br>
        2. 视频动画将优先于普通淡入动画<br>
        3. 如不需要视频动画，清空路径即可</small>""")
        note_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        layout.addWidget(note_label)
        
        layout.addStretch()

    def browse_video_file(self):
        """浏览选择视频文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "", 
            "视频文件 (*.mp4 *.avi *.mov *.mkv);;所有文件 (*)"
        )
        if file_path:
            self.video_path_edit.setText(file_path)

    def save_video_settings(self):
        """保存视频设置"""
        video_path = self.video_path_edit.text()
        self.settings.setValue("video_animation_path", video_path)
        
        # 可以添加提示信息
        self.apply_video_btn.setText("已设置")
        from PyQt6.QtCore import QTimer
        QTimer.singleShot(2000, lambda: self.apply_video_btn.setText("设置为启动动画"))

    def load_settings(self):
        """加载保存的设置"""
        # 加载动画启用状态
        enable_anim = self.settings.value("enable_animation", True, type=bool)
        self.anim_checkbox.setChecked(enable_anim)
        
        # 加载视频路径
        video_path = self.settings.value("video_animation_path", "", type=str)
        self.video_path_edit.setText(video_path)
        
        # 连接信号
        self.anim_checkbox.stateChanged.connect(
            lambda: self.settings.setValue("enable_animation", self.anim_checkbox.isChecked())
        )

    def is_animation_enabled(self):
        """检查是否启用动画"""
        return self.anim_checkbox.isChecked()

    def get_video_path(self):
        """获取视频路径"""
        return self.video_path_edit.text()