from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import face_recognition
from face_detection import Ui_MainWindow
import cv2
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cap = cv2.VideoCapture()
        self.widget_set()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_normal)
        # self.timer.timeout.disconnect(self.show_picture)

    def open_camera(self):
        number = self.comboBox.currentIndex()
        flag = self.cap.open(number)
        if flag is False:
            QMessageBox.information(self, "警告", "该设备未正常工作", QMessageBox.Ok)
        else:
            self.label.setEnabled(True)
            self.openbutton.setEnabled(False)
            self.closebutton.setEnabled(True)
            self.timer.start()

    def close_camera(self):
        self.cap.release()
        self.openbutton.setEnabled(True)
        self.closebutton.setEnabled(False)
        self.timer.stop()
        self.label.setText(" ")

    def normal_mode(self):
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.show_normal)
        self.facebutton.setEnabled(True)
        self.normalbutton.setEnabled(False)

    def face_mode(self):
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.show_face)
        self.facebutton.setEnabled(False)
        self.normalbutton.setEnabled(True)

    def widget_set(self):
        self.openbutton.clicked.connect(self.open_camera)
        self.closebutton.clicked.connect(self.close_camera)
        self.normalbutton.clicked.connect(self.normal_mode)
        self.facebutton.clicked.connect(self.face_mode)
        self.openbutton.setEnabled(True)
        self.closebutton.setEnabled(False)
        self.normalbutton.setEnabled(False)

    def show_normal(self):
        ret, frame = self.cap.read()
        if ret:
            if frame is not None:
                cur_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width = cur_frame.shape[:2]
                pixmap = QImage(cur_frame, width, height, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(pixmap)
                ratio = max(width/self.label.width(), height/self.height())
                pixmap.setDevicePixelRatio(ratio)
                self.label.setAlignment(Qt.AlignCenter)
                self.label.setPixmap(pixmap)

    def show_face(self):
        ret, frame = self.cap.read()
        if ret:
            if frame is not None:
                face_CNN = face_recognition.face_locations(frame)
                cur_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if len(face_CNN)  == 1:
                    top = face_CNN[0][0]
                    right = face_CNN[0][1]
                    bottom = face_CNN[0][2]
                    left = face_CNN[0][3]

                    cv2.rectangle(cur_frame, (left, top), (right, bottom), (0, 255, 255), 2)  # opencv 里面画矩形的函数
                height, width = cur_frame.shape[:2]
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
