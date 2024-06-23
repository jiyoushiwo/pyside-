# pyside2-uic untitled1.ui - ooutput.py        ui转py


# import random
# import sys
import cv2
import numpy as np

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QComboBox
global_i = 0

class MainWin:
    def __init__(self):
        # super().__init__()
        self.ui = QUiLoader().load("ui/test.ui")
        self.ui.pushButton.clicked.connect(self.clicked_open)
        self.ui.pushButton_2.clicked.connect(self.clicked_close)
        self.ui.pushButton_3.clicked.connect(self.clicked_renlian)
        self.ui.comboBox.currentIndexChanged.connect(self.clicked_combobox)#控件应用
        self.cap = None

    def clicked_combobox(self):
        print(self.ui.comboBox.currentIndex())#print(ComboBox.currentIndex(), ComboBox.currentText())
        global global_i
        global_i = self.ui.comboBox.currentIndex()
    def clicked_open(self):
        self.ui.label_1.setText('已打开摄像头')
        self.cap = cv2.VideoCapture(global_i)
        print('打开')
        # print()
        while True:
            ret, frame = self.cap.read()
            # cv2.imshow('frame', frame)

            if ret:
                # 将视频帧转换为RGB格式
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 将视频帧转换为PySide2的QImage格式
                height, width, channel = frame_rgb.shape
                bytes_per_line = 3 * width
                q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
                # 将QImage显示在QLabel中
                pixmap = QPixmap.fromImage(q_image)
                self.ui.label_1.setPixmap(pixmap)
            if cv2.waitKey(1) == ord('q'):
                # cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
    def clicked_close(self):
        self.cap.release()
        self.ui.label_2.setText('已关闭摄像头')
        print('关闭')
        self.ui.label_1.clear()
        self.ui.label_1.setText('图像关闭')
        if self.cap is not None:
            self.cap.release()
            # print("1")
            cv2.destroyAllWindows()

    def clicked_renlian(self):
        face_cascade = cv2.CascadeClassifier(
            r'D:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(global_i)
        while True:
            ret, frame = self.cap.read()
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 检测脸部
            faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
            print('Detected ', len(faces), " face")
            # 在图片中显示检测到的人脸数
            for (x, y, w, h) in faces:
                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # cv2.circle(iqmg, (int((x + x + w) / 2), int((y + y + h) / 2)), int(w / 2), (0, 255, 0), 1)
                # roi_gray = img_gray[y: y + h, x: x + w]
                # roi_color = img[y: y + h, x: x + w]
                label = 'Result: Detected ' + str(len(faces)) + " faces !"
                cv2.putText(frame, label, (10, 20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (255, 0, 0), 1)
            # 显示图片
            # cv2.imshow('img', frame)
            if ret:
                # 将视频帧转换为RGB格式
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 将视频帧转换为PySide2的QImage格式
                height, width, channel = frame_rgb.shape
                bytes_per_line = 3 * width
                q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
                # 将QImage显示在QLabel中
                pixmap = QPixmap.fromImage(q_image)
                self.ui.label_1.setPixmap(pixmap)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == "__main__":
    app = QApplication([])
    maindow = MainWin()
    maindow.ui.show()
    app.exec_()