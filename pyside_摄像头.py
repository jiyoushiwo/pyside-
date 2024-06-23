import cv2
from PySide2.QtWidgets import *
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Qt, QTimer

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.camera = cv2.VideoCapture(0)  # Use the default camera (index 0)
        self.is_camera_running = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update frame every 30 milliseconds (adjust as needed)

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("摄像头画面显示区域")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.toggle_button = QPushButton("开关摄像头")
        self.toggle_button.clicked.connect(self.toggle_camera)
        layout.addWidget(self.toggle_button)

        self.setCentralWidget(central_widget)

        self.setWindowTitle("Camera App")
        self.setGeometry(100, 100, 640, 480)

    def update_frame(self):
        face_cascade = cv2.CascadeClassifier(
            r'D:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
        if self.is_camera_running:
            ret, frame = self.camera.read()
            if ret:
                img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(img_gray, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
                for x, y, w, h in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_image)
                self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def toggle_camera(self):
        if self.is_camera_running:
            self.camera.release()
        else:
            self.camera = cv2.VideoCapture(0)
        self.is_camera_running = not self.is_camera_running

if __name__ == '__main__':
    app = QApplication([])

    window = CameraApp()
    window.show()

    app.exec_()
