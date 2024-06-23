import time
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *

class ChartLineSeries(QMainWindow):
    def __init__(self, parent=None):
        super(ChartLineSeries, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('QChart折线图演示')
        # 设置窗口大小
        self.resize(480, 360)
        self.createChart()

    def createChart(self):
        self.lineSeries = QLineSeries()
        self.chart = QChart()
        self.chart.setTitle("测试")
        self.axisX = QDateTimeAxis()#声明X，Y轴
        self.axisY = QValueAxis()
        self.axisX.setMin(QDateTime.currentDateTime().addSecs(-300))
        self.axisX.setMax(QDateTime.currentDateTime().addSecs(0))
        self.axisX.setFormat("hh:mm:ss")
        self.axisX.setTickCount(6)
        self.axisY.setTickCount(11)


        self.axisX.setTitleText("时间")
        self.axisY.setTitleText("温度")
        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        self.lineSeries.attachAxis(self.axisX)
        self.lineSeries.attachAxis(self.axisY)
        # 设置折线数据
        bjtime = QDateTime.currentDateTime()
        lineSeries = QLineSeries()
        # lineSeries.append(0, 6)
        # lineSeries.append(2, 4)
        # lineSeries.append(3, 8)
        # lineSeries.append(7, 4)
        # lineSeries.append(10, 5)
        # lineSeries.append(11, 1)
        # lineSeries.append(13, 3)
        # lineSeries.append(17, 6)
        # lineSeries.append(18, 3)
        # lineSeries.append(20, 2)

        # 创建图表

        chart = QChart()
        chart.y_Aix = QValueAxis()

        chart.legend().hide()
        chart.addSeries(lineSeries)#将点绘制在图表中
        # chart.createDefaultAxes()#使用默认坐标系
        chart.setTitle('折线图')#设置表的名称


        # chart.y_Aix.setTitleText("温度")

        # 图表视图
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartView)

    def drawLine(self):
        # 获取当前时间
        bjtime = QDateTime.currentDateTime()
        # 更新X轴坐标
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-self.showTime * 1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        # 当曲线上的点超出X轴的范围时，移除最早的点
        if self.series.count() > self.totalNum:
            self.series.removePoints(0, self.series.count() - self.totalNum)
        # 产生随机数
        yint = random.randint(-250, 250)
        # 添加数据到曲线末端
        self.series.append(bjtime.toMSecsSinceEpoch(), yint)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChartLineSeries()
    window.show()
    sys.exit(app.exec())



