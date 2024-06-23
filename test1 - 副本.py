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

        # self.ui.plainTextEdit
        content = self.ui.plainTextEdit.toPlainText()
        self.camera = cv2.VideoCapture(content, cv2.CAP_DSHOW)



        self.is_camera_running = True
        self.timer = QTimer()

        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 这两行代码的组合是确保定期更新摄像头画面的关键。每隔30毫秒更新一次摄像头画面。
        # ,self.update_frame方法，这样每当QTimer超时时，都会调用self.update_frame方法来更新摄像头画面。
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
            print("选中的选项:", button.text())
    def open(self):
        print("open")
        if not self.is_camera_running:
            self.camera = cv2.VideoCapture(0)
            self.is_camera_running = True

    def close(self):
        print("close")
        if self.is_camera_running:
            self.camera.release()
            self.is_camera_running = False


if __name__ == '__main__':
    app = QApplication([])  # 创建Qt应用程序的实例

    gui = Mainwindow()  # 创建一个名为Mainwindow的对象实例
    gui.ui.show()  # 显示界面
    app.exec_()  # 启动Qt应用程序的主事件循环，等待用户交互和事件响应，直到用户关闭了应用程序窗口或显式终止了应用程序的运行。
