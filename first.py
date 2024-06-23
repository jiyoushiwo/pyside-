from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox
from PySide2.QtGui import QIcon

app = QApplication([])
def handleCalc():
    print("按钮被点击")
    info = textEdit.toPlainText()#获取编辑框中的内容，toPlainText()函数将编辑框中的内容输出为一个字符串

    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():#splitlines()函数，返回一个包含各行作为元素的列表
        if not line.strip():#返回移除字符串头尾指定的字符生成的新字符串。
            continue

        parts = line.split(' ')
        print(parts)
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        print(parts)
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                      '统计结果',
                      f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                      )



window = QMainWindow()
window.resize(500, 400)
window.move(300, 300)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)#QPlainTextEdit 是一个多行文本编辑器，用于显示和编辑多行简单文本。
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)

window = QMainWindow()#实例化一个主窗口
window.resize(500, 400)#窗口的大小
window.move(300, 310)#主窗口的 左上角坐标在 相对屏幕的左上角 的X横坐标300像素, Y纵坐标310像素这个位置。
window.setWindowTitle('薪资统计')#窗口名称

textEdit = QPlainTextEdit(window)#在主窗口中放置一个文本编辑框
textEdit.setPlaceholderText("请输入薪资表")#占位提示文本
textEdit.move(10,25)#文本框的 左上角坐标在 相对父窗口的左上角 的X横坐标10像素, Y纵坐标25像素这个位置。
textEdit.resize(300,350)#文本框的大小

button = QPushButton('统计', window)#实例化一个按钮，名称为“统计”
button.move(380,80)#按钮的位置设置
button.clicked.connect(handleCalc)

window.show()#显示
app.setWindowIcon(QIcon('img.png'))#设置程序的图标，png文件要拷贝到程序的所在目录下

app.exec_()#