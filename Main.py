# @autor: Karol Siegieda
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.gui.GUIMainWindow import GUI_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI_MainWindow()
    window.show()
    app.exec_()