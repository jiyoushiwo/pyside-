from PySide2.QtWidgets import QApplication, QMainWindow, QRadioButton, QVBoxLayout, QWidget

class RadioButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.radio_button1 = QRadioButton("选项1", self)
        self.radio_button2 = QRadioButton("选项2", self)
        self.radio_button3 = QRadioButton("选项3", self)

        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(self.radio_button3)

        self.radio_button1.setChecked(True)  # 设置初始选中状态

        self.radio_button1.clicked.connect(lambda: self.on_radio_button_clicked(self.radio_button1))
        self.radio_button2.clicked.connect(lambda: self.on_radio_button_clicked(self.radio_button2))
        self.radio_button3.clicked.connect(lambda: self.on_radio_button_clicked(self.radio_button3))

    def on_radio_button_clicked(self, button):
        if button.isChecked():
            print("选中的选项:", button.text())

if __name__ == "__main__":
    app = QApplication([])
    window = RadioButtonExample()
    window.show()
    app.exec_()
