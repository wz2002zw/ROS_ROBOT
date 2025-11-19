from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QLineEdit, 
                             QGroupBox, QRadioButton, QFileDialog,
                             QMessageBox, QCheckBox, QApplication, QMainWindow,
                             QSplashScreen, QDialog)
from PyQt6.QtCore import Qt, QSettings, QTimer, QUrl, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QFont, QPixmap, QMovie, QIntValidator
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
import sys
import os


class SystemSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("ROS_Robot_UI", "StartupAnimation")
        self.init_ui()
        self.load_saved_settings()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # 标题
        title_label = QLabel("启动动画设置")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # 动画启用开关
        self.anim_enable_checkbox = QCheckBox("启用启动动画")
        self.anim_enable_checkbox.setChecked(True)
        main_layout.addWidget(self.anim_enable_checkbox)

        # 动画持续时间设置
        duration_layout = QHBoxLayout()
        self.duration_edit = QLineEdit()
        self.duration_edit.setPlaceholderText("输入动画持续时间（秒，默认3秒）")
        self.duration_edit.setValidator(QIntValidator(1, 10))
        duration_layout.addWidget(QLabel("动画时长:"))
        duration_layout.addWidget(self.duration_edit)
        duration_layout.addWidget(QLabel("秒（1-10秒）"))
        main_layout.addLayout(duration_layout)  # 添加到主布局

        # 动画类型选择
        type_group = QGroupBox("动画类型")
        type_layout = QVBoxLayout()
        self.video_radio = QRadioButton("视频动画")
        self.image_radio = QRadioButton("图片动画（支持静态图和GIF）")
        self.video_radio.setChecked(True)
        self.video_radio.clicked.connect(lambda: self.video_path_edit.setFocus())
        self.image_radio.clicked.connect(lambda: self.image_path_edit.setFocus())
        type_layout.addWidget(self.video_radio)
        type_layout.addWidget(self.image_radio)
        type_group.setLayout(type_layout)
        main_layout.addWidget(type_group)

        # 视频路径配置
        self.video_path_layout = QHBoxLayout()
        self.video_path_edit = QLineEdit()
        self.video_path_edit.setPlaceholderText("视频文件路径（支持MP4/AVI/MOV）")
        self.browse_video_btn = QPushButton("浏览视频")
        self.browse_video_btn.clicked.connect(self.browse_video)
        self.video_path_layout.addWidget(QLabel("视频路径:"))
        self.video_path_layout.addWidget(self.video_path_edit)
        self.video_path_layout.addWidget(self.browse_video_btn)
        main_layout.addLayout(self.video_path_layout)

        # 图片路径配置（支持GIF）
        self.image_path_layout = QHBoxLayout()
        self.image_path_edit = QLineEdit()
        self.image_path_edit.setPlaceholderText("图片文件路径（支持PNG/JPG/GIF）")
        self.browse_image_btn = QPushButton("浏览图片")
        self.browse_image_btn.clicked.connect(self.browse_image)
        self.image_path_layout.addWidget(QLabel("图片路径:"))
        self.image_path_layout.addWidget(self.image_path_edit)
        self.image_path_layout.addWidget(self.browse_image_btn)
        main_layout.addLayout(self.image_path_layout)

        # 按钮区
        btn_layout = QHBoxLayout()
        self.preview_btn = QPushButton("预览动画")
        self.preview_btn.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        self.preview_btn.clicked.connect(self.preview_animation)
        self.preview_btn.setStyleSheet("QPushButton { background-color: #e1f0fa; }")
        
        self.save_btn = QPushButton("保存设置")
        self.save_btn.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        self.save_btn.clicked.connect(self.save_settings)
        self.save_btn.setStyleSheet("QPushButton { background-color: #f0f0f0; }")
        
        btn_layout.addWidget(self.preview_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.save_btn)
        main_layout.addLayout(btn_layout)

        # 说明文本
        note_label = QLabel("""<small>
        <b>说明：</b><br>
        1. 视频动画优先于图片动画<br>
        2. 图片动画支持静态图（PNG/JPG）和动态图（GIF）<br>
        3. 若路径为空或文件不存在，将使用默认动画<br>
        4. 图片/GIF动画会显示3秒后自动关闭<br>
        5. 预览前请确保文件路径正确且文件可读取
        </small>""")
        note_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        main_layout.addWidget(note_label)

        main_layout.addStretch()

    # ------------------------------
    # 配置管理（保存/加载/路径选择）
    # ------------------------------
    def browse_video(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "", 
            "视频文件 (*.mp4 *.avi *.mov *.mkv);;所有文件 (*)"
        )
        if file_path:
            self.video_path_edit.setText(file_path)
            print(f"选择视频路径：{file_path}")

    def browse_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择图片文件", "", 
            "图片文件 (*.png *.jpg *.jpeg *.bmp *.gif);;所有文件 (*)"
        )
        if file_path:
            self.image_path_edit.setText(file_path)
            print(f"选择图片路径：{file_path}")

    def save_settings(self):
        self.settings.setValue("animation_enabled", self.anim_enable_checkbox.isChecked())
        self.settings.setValue("use_video", self.video_radio.isChecked())
        self.settings.setValue("video_path", self.video_path_edit.text())
        self.settings.setValue("image_path", self.image_path_edit.text())

        try:
            duration = int(self.duration_edit.text().strip())
            if duration < 1 or duration > 10:
                raise ValueError("超出范围")
            self.settings.setValue("animation_duration",duration)
        except:
            self.settings.setValue("animation_duration",3)

        QMessageBox.information(self, "保存成功", "启动动画设置已保存！")

    def load_saved_settings(self):
        enabled = self.settings.value("animation_enabled", True, type=bool)
        self.anim_enable_checkbox.setChecked(enabled)
        
        use_video = self.settings.value("use_video", True, type=bool)
        self.video_radio.setChecked(use_video)
        self.image_radio.setChecked(not use_video)
        
        video_path = self.settings.value("video_path", "", type=str)
        self.video_path_edit.setText(video_path)
        
        image_path = self.settings.value("image_path", "", type=str)
        if not image_path:
            default_image_path = "/home/wz/Desktop/ROS_ROBOT/src/test_moveit_config/UI/video_and_photos/preview.jpg"
            self.image_path_edit.setText(default_image_path)
            print(f"加载默认图片路径：{default_image_path}")
        else:
            self.image_path_edit.setText(image_path)
            print(f"加载保存的图片路径：{image_path}")

    # ------------------------------
    # 启动动画核心逻辑（供主页面调用）
    # ------------------------------
    def show_startup_animation(self, parent_window=None):
        """显示启动动画（主页面调用此方法）"""
        print("\n===== 启动动画逻辑开始 =====")
        
        animation_enabled = self.settings.value("animation_enabled", True, type=bool)
        print(f"动画启用状态: {animation_enabled}")
        if not animation_enabled:
            print("动画已被禁用，不显示启动动画")
            return

        use_video = self.settings.value("use_video", True, type=bool)
        video_path = self.settings.value("video_path", "", type=str).strip()
        image_path = self.settings.value("image_path", "", type=str).strip()
        
        print(f"动画类型: {'视频' if use_video else '图片'}")
        print(f"视频路径: {video_path}（是否存在: {os.path.exists(video_path) if video_path else False}）")
        print(f"图片路径: {image_path}（是否存在: {os.path.exists(image_path) if image_path else False}）")

        if use_video and video_path and os.path.exists(video_path):
            print(f"执行视频动画: {video_path}")
            self._play_video_animation(video_path)
        elif not use_video and image_path and os.path.exists(image_path):
            print(f"执行图片动画: {image_path}")
            self._show_image_animation(image_path)
        else:
            print("无有效动画路径，执行默认淡入动画")
            self._show_default_animation(parent_window)

        print("===== 启动动画逻辑结束 =====\n")

    # ------------------------------
    # 动画播放实现（内部方法）
    # ------------------------------
    def _play_video_animation(self, video_path):
        """播放视频启动动画"""
        try:
            splash_dialog = QDialog(None, 
                Qt.WindowType.FramelessWindowHint | 
                Qt.WindowType.WindowStaysOnTopHint
            )
            splash_dialog.setWindowTitle("启动中")
            splash_dialog.setModal(True)
            
            video_widget = QVideoWidget()
            layout = QVBoxLayout(splash_dialog)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(video_widget)
            
            player = QMediaPlayer()
            player.setVideoOutput(video_widget)
            player.setSource(QUrl.fromLocalFile(video_path))
            
            def close_dialog(status):
                if status == QMediaPlayer.MediaStatus.EndOfMedia:
                    print("视频播放结束，关闭动画窗口")
                    splash_dialog.close()
            
            player.mediaStatusChanged.connect(close_dialog)
            player.errorOccurred.connect(
                lambda e: (print(f"视频错误: {player.errorString()}"), splash_dialog.close())
            )
            
            splash_dialog.resize(800, 600)
            splash_dialog.move(
                QApplication.primaryScreen().geometry().center() - 
                splash_dialog.rect().center()
            )
            
            splash_dialog.show()
            player.play()
            QApplication.processEvents()
            splash_dialog.exec()
            
        except Exception as e:
            print(f"视频动画失败: {str(e)}")
            QMessageBox.warning(None, "视频动画失败", f"无法播放视频: {str(e)}")
            self._show_default_animation()

    def _show_image_animation(self, image_path):
        """显示图片/GIF启动动画（放大窗口尺寸）"""
        try:
            dialog = QDialog(None)
            dialog.setWindowTitle("系统启动中")
            dialog.setModal(True)
            dialog.setWindowFlags(
                Qt.WindowType.WindowStaysOnTopHint |
                Qt.WindowType.Dialog |
                Qt.WindowType.WindowTitleHint
            )

            layout = QVBoxLayout(dialog)
            layout.setContentsMargins(20, 20, 20, 20)

            # 获取屏幕尺寸（用于限制最大窗口大小）
            screen_geo = QApplication.primaryScreen().geometry()
            max_screen_width = int(screen_geo.width() * 0.8)  # 最大不超过屏幕宽度80%
            max_screen_height = int(screen_geo.height() * 0.8)  # 最大不超过屏幕高度80%

            if image_path.lower().endswith(('.gif', '.GIF')):
                movie = QMovie(image_path)
                if not movie.isValid():
                    raise Exception("GIF格式无效或文件损坏")
                
                original_size = movie.scaledSize()
                # 优化1：提高最大缩放比例到3倍（原2倍）
                max_scale = 3.0  
                # 计算基于缩放比例的最大尺寸
                scale_based_width = int(original_size.width() * max_scale)
                scale_based_height = int(original_size.height() * max_scale)
                # 取缩放比例和屏幕限制的最小值（避免超出屏幕）
                max_width = min(scale_based_width, max_screen_width)
                max_height = min(scale_based_height, max_screen_height)
                # 优化2：设置最小尺寸（避免过小，如宽高至少300px）
                max_width = max(max_width, 300)
                max_height = max(max_height, 300)

                scaled_size = original_size.scaled(
                    max_width, max_height,
                    Qt.AspectRatioMode.KeepAspectRatio
                )
                movie.setScaledSize(scaled_size)

                gif_label = QLabel()
                gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                gif_label.setStyleSheet("image-rendering: smooth;")
                gif_label.setMovie(movie)
                layout.addWidget(gif_label)
                movie.start()
                print(f"执行GIF启动动画（尺寸：{scaled_size.width()}x{scaled_size.height()}）")

            else:
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    raise Exception("图片格式不支持或文件损坏")
                
                # 优化3：静态图最大尺寸调整为屏幕80%，最小300px
                scaled_pixmap = pixmap.scaled(
                    max_screen_width, max_screen_height,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                # 确保图片不小于最小尺寸
                if scaled_pixmap.width() < 300 or scaled_pixmap.height() < 300:
                    scaled_pixmap = pixmap.scaled(
                        300, 300,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )

                image_label = QLabel()
                image_label.setPixmap(scaled_pixmap)
                image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(image_label)
                print(f"执行静态图片启动动画（尺寸：{scaled_pixmap.width()}x{scaled_pixmap.height()}）")

            # 提示文字
            hint_label = QLabel("仿真系统正在启动，请稍等哦😊")
            hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            hint_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            hint_label.setStyleSheet("color: #333; margin-top: 15px;")
            layout.addWidget(hint_label)

            # 窗口尺寸适配（加边距）
            if image_path.lower().endswith(('.gif', '.GIF')):
                dialog.resize(scaled_size.width() + 60, scaled_size.height() + 100)  # 增加边距
            else:
                dialog.resize(scaled_pixmap.width() + 60, scaled_pixmap.height() + 100)

            # 窗口居中
            dialog.move(
                (screen_geo.width() - dialog.width()) // 2,
                (screen_geo.height() - dialog.height()) // 2
            )

            dialog.show()
            QApplication.processEvents()
            duration_ms = self.settings.value("animation_duration", 3, type=int) * 1000
            
            def close_animation():
                if image_path.lower().endswith(('.gif', '.GIF')):
                    movie.stop()
                dialog.close()
            
            QTimer.singleShot(duration_ms, close_animation)
            dialog.exec()

        except Exception as e:
            print(f"图片/GIF动画失败: {str(e)}")
            QMessageBox.warning(None, "启动动画失败", f"无法显示图片/GIF: {str(e)}")
            self._show_default_animation()

    def _show_default_animation(self, parent_window=None):
        """默认淡入动画（需要主窗口实例）"""
        if parent_window:
            parent_window.hide()
            parent_window.setWindowOpacity(0.0)
            parent_window.show()
            
            opacity_anim = QPropertyAnimation(parent_window, b"windowOpacity")
            opacity_anim.setDuration(1500)
            opacity_anim.setStartValue(0.0)
            opacity_anim.setEndValue(1.0)
            opacity_anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
            opacity_anim.start()
            
            QApplication.processEvents()
        else:
            # 若无主窗口，显示简单提示
            dialog = QDialog(None)
            dialog.setWindowTitle("启动中")
            dialog.setModal(True)
            dialog.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
            dialog.resize(300, 150)
            dialog.move(QApplication.primaryScreen().geometry().center() - dialog.rect().center())
            dialog.setLayout(QVBoxLayout())
            dialog.layout().addWidget(QLabel("系统启动中...", alignment=Qt.AlignmentFlag.AlignCenter))
            dialog.show()
            QTimer.singleShot(1500, dialog.close)
            dialog.exec()

    # ------------------------------
    # 预览功能（与启动动画逻辑复用）
    # ------------------------------
    def preview_animation(self):
        """预览动画（复用启动动画的核心方法）"""
        print("\n===== 开始预览动画 =====")
        if not self.anim_enable_checkbox.isChecked():
            QMessageBox.information(self, "提示", "请先勾选“启用启动动画”")
            print("预览失败：未启用启动动画")
            return

        use_video = self.video_radio.isChecked()
        video_path = self.video_path_edit.text().strip()
        image_path = self.image_path_edit.text().strip()

        print(f"视频路径：{video_path}（是否存在：{os.path.exists(video_path)}）")
        print(f"图片路径：{image_path}（是否存在：{os.path.exists(image_path)}）")

        if use_video:
            if video_path and os.path.exists(video_path):
                print(f"开始播放视频预览：{video_path}")
                self._play_video_animation(video_path)  # 复用视频播放逻辑
            else:
                QMessageBox.warning(self, "路径无效", f"视频文件不存在或路径为空\n当前路径：{video_path}")
                print("视频路径无效，显示默认动画")
                self._show_default_preview()
        else:
            if image_path and os.path.exists(image_path):
                if image_path.lower().endswith(('.gif', '.GIF')):
                    print(f"开始显示GIF预览：{image_path}")
                    self._show_gif_preview(image_path)
                else:
                    print(f"开始显示图片预览：{image_path}")
                    self._show_image_preview(image_path)
            else:
                QMessageBox.warning(self, "路径无效", f"图片文件不存在或路径为空\n当前路径：{image_path}")
                print("图片路径无效，显示默认动画")
                self._show_default_preview()

    def _show_image_preview(self, image_path):
        """静态图片预览（放大窗口）"""
        try:
            if not os.access(image_path, os.R_OK):
                raise Exception("文件无读取权限")
            
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                raise Exception("图片格式不支持或文件损坏")
            
            # 屏幕尺寸限制
            screen_geo = QApplication.primaryScreen().geometry()
            max_screen_width = int(screen_geo.width() * 0.8)
            max_screen_height = int(screen_geo.height() * 0.8)
            
            scaled_pixmap = pixmap.scaled(
                max_screen_width, max_screen_height,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            # 确保最小尺寸300px
            if scaled_pixmap.width() < 300 or scaled_pixmap.height() < 300:
                scaled_pixmap = pixmap.scaled(
                    300, 300,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

            dialog = QDialog(self)
            dialog.setWindowTitle("图片动画预览")
            dialog.setModal(True)
            dialog.setWindowFlags(
                Qt.WindowType.WindowStaysOnTopHint |
                Qt.WindowType.Dialog | 
                Qt.WindowType.WindowTitleHint
            )
            
            layout = QVBoxLayout(dialog)
            image_label = QLabel()
            image_label.setPixmap(scaled_pixmap)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(image_label)
            
            hint_label = QLabel(f"图片预览（{self.settings.value('animation_duration', 3)}秒后自动关闭）")
            hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            hint_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            layout.addWidget(hint_label)
            
            # 增加边距
            dialog.resize(scaled_pixmap.width() + 60, scaled_pixmap.height() + 100)
            dialog.move(
                (screen_geo.width() - dialog.width()) // 2,
                (screen_geo.height() - dialog.height()) // 2
            )
            
            dialog.show()
            QApplication.processEvents()
            duration_ms = self.settings.value("animation_duration", 3, type=int) * 1000
            QTimer.singleShot(duration_ms, dialog.close)
            
        except Exception as e:
            QMessageBox.critical(self, "显示失败", f"图片预览出错：{str(e)}")
            print(f"图片预览异常：{str(e)}")
            self._show_default_preview()
    def _show_gif_preview(self, gif_path):
        """GIF预览（放大预览窗口）"""
        try:
            if not os.access(gif_path, os.R_OK):
                raise Exception("文件无读取权限")
            
            movie = QMovie(gif_path)
            if not movie.isValid():
                raise Exception("GIF格式无效或文件损坏")
            
            # 同样应用屏幕比例限制
            screen_geo = QApplication.primaryScreen().geometry()
            max_screen_width = int(screen_geo.width() * 0.8)
            max_screen_height = int(screen_geo.height() * 0.8)
            
            original_size = movie.scaledSize()
            max_scale = 3.0  # 放大到3倍
            scale_based_width = int(original_size.width() * max_scale)
            scale_based_height = int(original_size.height() * max_scale)
            max_width = min(scale_based_width, max_screen_width)
            max_height = min(scale_based_height, max_screen_height)
            max_width = max(max_width, 300)  # 最小300px
            max_height = max(max_height, 300)

            scaled_size = original_size.scaled(
                max_width, max_height,
                Qt.AspectRatioMode.KeepAspectRatio
            )
            movie.setScaledSize(scaled_size)
            
            dialog = QDialog(self)
            dialog.setWindowTitle("GIF动画预览")
            dialog.setModal(True)
            dialog.setWindowFlags(
                Qt.WindowType.WindowStaysOnTopHint |
                Qt.WindowType.Dialog | 
                Qt.WindowType.WindowTitleHint
            )
            
            layout = QVBoxLayout(dialog)
            gif_label = QLabel()
            gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            gif_label.setStyleSheet("image-rendering: smooth;")
            gif_label.setMovie(movie)
            layout.addWidget(gif_label)
            
            hint_label = QLabel(f"GIF预览（{self.settings.value('animation_duration', 3)}秒后自动关闭）")
            hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            hint_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            layout.addWidget(hint_label)
            
            # 增加边距使窗口更大
            dialog.resize(scaled_size.width() + 60, scaled_size.height() + 100)
            dialog.move(
                (screen_geo.width() - dialog.width()) // 2,
                (screen_geo.height() - dialog.height()) // 2
            )
            
            dialog.show()
            movie.start()
            QApplication.processEvents()
            duration_ms = self.settings.value("animation_duration", 3, type=int) * 1000
            QTimer.singleShot(duration_ms, lambda: (movie.stop(), dialog.close()))
            
        except Exception as e:
            QMessageBox.critical(self, "显示失败", f"GIF预览出错：{str(e)}")
            print(f"GIF预览异常：{str(e)}")
            self._show_default_preview()

    def _show_default_preview(self):
        """默认预览（无有效文件时）"""
        dialog = QDialog(self)
        dialog.setWindowTitle("默认预览")
        dialog.setModal(True)
        dialog.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Dialog)
        
        layout = QVBoxLayout(dialog)
        label = QLabel("无有效动画文件，将使用默认启动效果")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        
        dialog.resize(300, 150)
        dialog.move(QApplication.primaryScreen().geometry().center() - dialog.rect().center())
        dialog.show()
        QTimer.singleShot(2000, dialog.close)
        dialog.exec()

    # 外部访问接口
    def is_animation_enabled(self):
        return self.anim_enable_checkbox.isChecked()

    def use_video_animation(self):
        return self.video_radio.isChecked()

    def get_video_path(self):
        return self.video_path_edit.text()

    def get_image_path(self):
        return self.image_path_edit.text()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("ROS_Robot_UI")
    app.setOrganizationName("ROS_Robot")
    
    test_window = QMainWindow()
    test_window.setWindowTitle("系统设置测试（支持GIF）")
    test_window.setGeometry(100, 100, 600, 400)
    test_window.setCentralWidget(SystemSettingsWidget())
    test_window.show()
    
    sys.exit(app.exec())