# @autor: Karol Siegieda
import sys, os, subprocess
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QApplication
from src.gui.MainWindow import GUI_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI_MainWindow()

    dateUpdate = QTimer()
    dateUpdate.timeout.connect(window.setSystemTime)
    dateUpdate.start(10000)

    window.show()
    app.exec_()