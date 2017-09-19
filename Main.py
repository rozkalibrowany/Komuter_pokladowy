# @autor: Karol Siegieda, Michal Sut

import sys
from PyQt4 import QtCore, QtGui

#from src.gui.MainWindow import Ui_MainWindow

from src.gui.Window import Ui_MainWindow as Ui_Window
#from BmsWindow import Ui_Form
#from keyboard import *
import test
from datetime import datetime
import random
import subprocess
from functools import partial
from src.modules.utils import *
import math
from src.gui.widgets import RPM_Widget


systemStatus = 0
connectionStatus = 0
s = 0
m = 0
ms = 0
timerStarted = False
lapTimesCounter = 0

# constant values
MAX_RPM_VALUE = 6000
MAX_TEMPERATURE_VALUE = 255
ANGLE_RANGE = 245

class StopwatchThread(QtCore.QThread):

    setmiliseconds = QtCore.pyqtSignal([int])
    setseconds = QtCore.pyqtSignal([int])
    setminutes = QtCore.pyqtSignal([int])
    setTime = QtCore.pyqtSignal([QtCore.QTime])

    def __init__(self):
        super(StopwatchThread, self).__init__()
        self._isRunning = False


    def run(self):
        self.initialTime = datetime.now()
        self. prev_miliseconds = 0
        while self._isRunning:

            elapsedTime = datetime.now() - self.initialTime
            miliseconds = elapsedTime.microseconds/1000
            if miliseconds != self.prev_miliseconds:
                time = QtCore.QTime(elapsedTime.seconds/60,elapsedTime.seconds,miliseconds)
                self.setTime.emit(time)

            self.prev_miliseconds = miliseconds

    def stop(self):
        self._isRunning = False

    def start(self):
        super(StopwatchThread, self).start()
        self._isRunning = True

class GUI_Window(QtGui.QMainWindow, Ui_Window):
    def __init__(self, parent=None):
        super(GUI_Window, self).__init__(parent)
        self.setupUi(self)
##        self.w = Ui_rpm_widget()
        self.gg = RPM_Widget(self.rpm_widget)
        self.activateDial = True


        self.init_temp_widget()

        self.proc = QtCore.QProcess()
        self.proc.readyReadStandardOutput.connect(partial(self.updateScreen, self.proc))
        self.isActive = False
        self.btnStart.clicked.connect(self.toggleActive)
        self.prev_temp = 0
        self.isConnected = False
        self.btnConnect.clicked.connect(self.toggleConnect)
        self.btnStopwatch.clicked.connect(self.toggleStopwatch)
        self.isStopwatchRunning = False
        self.stopwatch = StopwatchThread()
        self.stopwatch.setTime.connect(self.timeEdit.setTime)
        
    def init_temp_widget(self):
        self.scene_temp = QtGui.QGraphicsScene()
        self.tempBar.setScene(self.scene_temp)
        self.tempBar.setSceneRect(0,0,self.tempBar.frameSize().width(),self.tempBar.frameSize().height())
        self.tempBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.tempBar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);

    def toggleActive(self):
        if self.isActive:
            self.isActive = False
            self.btnStart.setText("START")
        else:
            self.isActive = True
            self.btnStart.setText("STOP")

    def toggleConnect(self):
        if self.isConnected:
            self.proc.kill()
            self.isConnected = False
            self.btnConnect.setText("Connect")
            self.labelStatus.setText("Not connected")
            self.labelStatus.setStyleSheet("color: red; background: none;")
            self.updateScreen(clear=True)
        else:
            self.proc.setProcessChannelMode(self.proc.MergedChannels)
            self.proc.start("stdbuf -o0 candump can0")
            self.isConnected = True
            self.btnConnect.setText("Disconnect")
            self.labelStatus.setText("Connected")
            self.labelStatus.setStyleSheet("color: green; background: none;")

    def toggleStopwatch(self):
        if self.isStopwatchRunning:
            self.stopwatch.stop()
            self.btnStopwatch.setText("Start")
            self.isStopwatchRunning = False
        else:
            self.stopwatch.start()
            self.btnStopwatch.setText("Stop")
            self.isStopwatchRunning = True


    def updateScreen(self, proc=None, clear=False):
        if not clear:
            lineunsplitted =  str(proc.readAllStandardOutput()).strip()
            line =  lineunsplitted.split()
            self.framesLabel.setText(lineunsplitted)
            if(line[1] == "0CF11E05"):
                rpm_lsb = int(line[3], base=16)
                rpm_msb = int(line[4], base=16)
                rpm_dec = rpm_msb * 256 + rpm_lsb
                print (rpm_dec)
            engine_temp = int(line[4], base=16)
            voltage = int(line[5], base=16)
            current = int(line[6], base=16)
        else:
            rpm = 0
            engine_temp = 0
            voltage = 0
            current = 0

        if self.isActive and line[1] == "0CF11E05":
            self.gg.updateRPM(rpm_dec)
            self.updateEngineTemp(engine_temp)
            self.updateVoltage(voltage)
            self.updateCurrent(current)


    def updateEngineTemp(self, temp):
        if self.activateDial:
            temp = self.dial.value()

        max_height = self.tempBar.height()

        if self.prev_temp:
            avg_temp = (self.prev_temp + temp)/2
        else:
            avg_temp = temp

        scaled_temp = temp * max_height/float(MAX_TEMPERATURE_VALUE)
        self.tempNumber.setText(format_temp(avg_temp))
        rgb = temp_to_rgb_blue(avg_temp)
        #self.tempBarWhite.setStyleSheet("QLabel {background-color: rgb" + str(rgb) + ";}")

##        rect = QtCore.QRect(self.tempBarWhite.x(), self.tempBarWhite.y(), self.tempBarWhite.width(),scaled_temp)
##        self.tempBarWhite.setGeometry(rect)
        self.prev_temp = temp

        r,g,b = rgb
        self.scene_temp.clear()
        rectItem = QtGui.QGraphicsRectItem(0, max_height-scaled_temp, self.tempBar.width(), scaled_temp)
        rectItem.setBrush(QtGui.QBrush(QtGui.QColor(r,g,b)))
        self.scene_temp.addItem(rectItem)


    def updateVoltage(self, voltage):
        self.voltageBar.setValue(voltage)

    def updateCurrent(self, current):
        self.currentBar.setValue(current)





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    x = GUI_Window()
    x.show()

    app.exec_()
