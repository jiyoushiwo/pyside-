from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile,QTimer
from PyQt5.QtGui import QImage, QPixmap
from PySide2.QtGui import QIcon
import cv2

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_stats = QFile(r"C:\Users\李政轩\PycharmProjects\pythonProject\opencv\ui.ui")#"C:\Users\李政轩\PycharmProjects\pythonProject\pyside2\untitled.ui"
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_stats)

        self.ui.pushButton.clicked.connect(self.my_timer_cb)



        '''自定义部分'''
        self.my_timer = QTimer()  # 创建定时器
        self.my_timer.timeout.connect(self.my_timer_cb)  # 创建定时器任务

        '''按钮状态控制'''
        self.btn_status = False

    '''加载所有的命令'''

    def action_list(self):
        self.btn_start()

    '''所有命令详细定义'''

    def btn_start(self):
        if self.btn_status:
            self.btn_status = False
        else:
            self.btn_status = True

        if self.btn_status:
            self.ui.pushButton.setText('关闭摄像头')
            self.my_timer.start(40)  # 25fps
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # start camera
        else:
            self.ui.pushButton.setText('开启摄像头')
            self.ui.label.clear()  # 清楚label内容
            self.my_timer.stop()  # 停止定时器
            self.cap.release()  # 关闭摄像头

    def my_timer_cb(self):
        self.cap = cv2.VideoCapture(0)
        if self.cap:
            """图像获取"""
            ret, self.image = self.cap.read()
            show = cv2.resize(self.image, (640, 480))
            show = cv2.flip(show, 1)
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

            """图像处理"""

            """处理结果存储"""

            """结果呈现"""
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.ui.label.setPixmap(QPixmap.fromImage(showImage))



if __name__=="__main__":
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.setWindowIcon(QIcon('img.png'))  # 设置程序的图标，png文件要拷贝到程序的所在目录下
    app.exec_()
