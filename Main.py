# @autor: Karol Siegieda
import sys, os, subprocess
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QApplication
from src.gui.MainWindow import GUI_MainWindow
from src.gui.RadialBar import *
from PyQt5.QtQml import *
from src.gui.RadialBar import RadialBar
from OpenGL import GLU


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI_MainWindow()

    batteryCurrentWidget = BatteryCurrentWidget()
    context = window.batteryCWidget.rootContext()
    context.setContextProperty("batteryCurrentWidget", batteryCurrentWidget)
    window.batteryCWidget.setSource(QUrl.fromLocalFile('src/gui/batteryCurrentRadialBar.qml'))

    batteryVoltageWidget = BatteryVoltageWidget()
    context = window.batteryVWidget.rootContext()
    context.setContextProperty("batteryVoltageWidget",batteryVoltageWidget)
    window.batteryVWidget.setSource(QUrl.fromLocalFile('src/gui/batteryVoltageRadialBar.qml'))

    batteryTempWidget = BatteryTempWidget()
    context = window.batteryTWidget.rootContext()
    context.setContextProperty("batteryTempWidget",batteryVoltageWidget)
    window.batteryTWidget.setSource(QUrl.fromLocalFile('src/gui/batteryTempRadialBar.qml'))

    contrTempWidget = ContrTempWidget()
    context = window.contrTWidget.rootContext()
    context.setContextProperty("contrTempWidget",contrTempWidget)
    window.contrTWidget.setSource(QUrl.fromLocalFile('src/gui/contrTempRadialBar.qml'))

    timer = QTimer()
    timer.timeout.connect(batteryCurrentWidget.random_value)
    timer.timeout.connect(batteryVoltageWidget.random_value)
    timer.timeout.connect(batteryTempWidget.random_value)
    timer.timeout.connect(contrTempWidget.random_value)
    timer.start(100)
    window.show()
    sys.exit(app.exec_())