from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import cv2
from PySide2.QtWidgets import *
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Qt, QTimer

class Mainwindow(object):
    def __init__(self):
        # 对ui文件进行加载
        self.ui = QUiLoader().load('ui/untitled.ui')
        self.ui.button1.clicked.connect(self.open)
        self.ui.button.clicked.connect(self.close)
        self.ui.button2.clicked.connect(self.print_plain_text)

        self.ui.radioButton1.clicked.connect(lambda: self.on_radio_button_clicked(self.ui.radioButton1))
        self.ui.radioButton2.clicked.connect(lambda: self.on_radio_button_clicked(self.ui.radioButton2))

        # 设置初始视频源
        self.video_source = 0  # 默认为设备ID为0的摄像头

        self.camera = cv2.VideoCapture(self.video_source, cv2.CAP_DSHOW)

        self.is_camera_running = True
        self.timer = QTimer()

        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        if self.is_camera_running:
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_image)
                self.ui.label.setPixmap(pixmap.scaled(self.ui.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def print_plain_text(self):
        content = self.ui.plainTextEdit.toPlainText()
        print(content)

    def on_radio_button_clicked(self, button):
        if button.isChecked():
            if button.text() == "选项1":
                self.video_source = 0  # 设置视频源为设备ID为0的摄像头
            elif button.text() == "选项2":
                # 设置视频源为另一个摄像头的ID（例如，设备ID为1的摄像头）
                self.video_source = 1

            # 释放当前摄像头
            self.camera.release()
            # 打开新的摄像头
            self.camera.open(self.video_source)
            # 重新启动定时器，保证更新新的摄像头画面
            self.timer.start()

    def open(self):
        print("open")
        if not self.is_camera_running:
            self.camera.open(self.video_source)
            self.is_camera_running = True

    def close(self):
        print("close")
        if self.is_camera_running:
            self.camera.release()
            self.is_camera_running = False
            # 停止定时器，防止不必要的更新
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication([])

    gui = Mainwindow()
    gui.ui.show()
    app.exec_()
