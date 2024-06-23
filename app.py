from PySide2.QtCore import Qt,QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

app = QApplication([])
window = QMainWindow()
window.resize(500, 400)
window.move(300, 300)

window.setWindowTitle('薪资统计')
def handleCalc():
    print("按钮被点击")
button = QPushButton('统计', window)#实例化一个按钮，名称为“统计”
button.move(380,80)#按钮的位置设置
button.clicked.connect(handleCalc)

# 设置图标
button.setIcon(QIcon('img.png'))

# 设置图标大小
button.setIconSize(QSize(30, 30))
window.show()#显示

app.exec_()#