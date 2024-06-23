import sys
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySideUI import Ui_MainWindow  # 从由ui文件转换而来的Py文件中导入主要函数
import cv2
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cap = cv2.VideoCapture()
        self.button_set()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_picture)

    def open_camera(self):
        number = self.comboBox.currentIndex()
        print(number)
        flag = self.cap.open(number)
        if flag is False:
            QMessageBox.information(self, "警告", "该设备未正常工作", QMessageBox.Ok)
        else:
            self.label.setEnabled(True)  # 此句感觉可删，待调试测试
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.timer.start()

    def close_camera(self):
        self.cap.release()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.timer.stop()
        self.label.setText(" ")

    def button_set(self):
        self.pushButton.clicked.connect(self.open_camera)
        self.pushButton_2.clicked.connect(self.close_camera)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)

    def show_picture(self):
        ret, frame = self.cap.read()
        if ret:
            if frame is not None:
                cur_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width = cur_frame.shape[:2]  # cur_frame=会返回图像的高、宽与颜色通道数，截前2
                pixmap = QImage(cur_frame, width, height, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(pixmap)
                ratio = max(width/self.label.width(), height/self.height())
                pixmap.setDevicePixelRatio(ratio)
                self.label.setAlignment(Qt.AlignCenter)
                self.label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    app.exec()

