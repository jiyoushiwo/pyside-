import time
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
from PyQt5.QtCore import QDateTime, Qt, QTimer
class DemoDateTimeAxis(QMainWindow):
    def __init__(self):
        super(DemoDateTimeAxis,self).__init__()
        self.setWindowTitle("测试")
        self.createChart()
    def createChart(self):


        series = QSplineSeries()
        xValue = QDateTime()
        xValue.setDate(QDate(2019,1,18))
        xValue.setTime(QTime(9,34))
        yValue = 12
        series.append(xValue.toMSecsSinceEpoch(),yValue)
        chart = QChart()#创建图表
        chart.legend().hide()
        chart.addSeries(series)#加载曲线
        chart.setTitle("数据测试")

        #坐标轴
        axisX = QDateTimeAxis()
        axisX.setTickCount(10)
        axisX.setFormat("mm:ss")
        axisX.setTitleText("时间")
        chart.addAxis(axisX,Qt.AlignBottom)
        series.attachAxis(axisX)

        #Y轴
        axisY = QValueAxis()
        axisY.setLabelFormat("%i")
        axisY.setTitleText("值")
        series.attachAxis(axisY)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)
if __name__=="__main__":
    app=QApplication(sys.argv)
    window = DemoDateTimeAxis()
    window.show()
    sys.exit(app.exec_())



chartView = QChartView()
chartView.chart().addSeries()

axisX = QDateTimeAxis()
axisX.setFormat("dd-MM-yy h:mm")
chartView.chart().setAxisX(axisX,series)