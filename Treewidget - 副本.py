
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QBrush
from PySide2.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QMainWindow, QStyle


class TreeWidgetDemo(QMainWindow):
    def __init__(self):
        super(TreeWidgetDemo, self).__init__()
        self.setWindowTitle("TreeWidget Demo")
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)#创建两列
        self.tree.setHeaderLabels(['Key', 'Value'])#命名

        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'group1')
        root.setIcon(0, self.style().standardIcon(QStyle.SP_DirIcon))

        self.tree.setColumnWidth(0, 150)
        ## 设置节点的背景颜色
        brush_red = QBrush(Qt.red)
        root.setBackground(0, brush_red)
        brush_green = QBrush(Qt.green)
        root.setBackground(1, brush_green)

        # 设置子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'ios')
        child1.setIcon(0, QIcon("img.png"))#设置图标
        child1.setCheckState(0, Qt.Checked)

        # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')#设置文本

        child2.setText(1, 'text')

        # 设置子节点3
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, 'android')

        self.tree.addTopLevelItem(root)
        # 结点全部展开
        self.tree.expandAll()

        self.setCentralWidget(self.tree)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec_())


