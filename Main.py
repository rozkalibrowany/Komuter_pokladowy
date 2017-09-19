# @autor: Karol Siegieda, Michal Sut

import sys
from PyQt4 import QtCore, QtGui

from MainWindow import Ui_MainWindow
from Window import Ui_MainWindow as Ui_Window
from BmsWindow import Ui_Form
from keyboard import *
import test
from datetime import datetime
import random
import subprocess
from functools import partial
from utils import *
import math


systemStatus = 0
connectionStatus = 0
s = 0
m = 0
ms = 0
timerStarted = False
lapTimesCounter = 0

# constant values
MAX_RPM_VALUE = 255
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
##            print miliseconds
            if miliseconds != self.prev_miliseconds:
                time = QtCore.QTime(elapsedTime.seconds/60,elapsedTime.seconds,miliseconds)
                self.setTime.emit(time)
                
            self.prev_miliseconds = miliseconds
##            
##            self.setmiliseconds.emit(elapsedTime.microseconds/1000/10)
##            self.setseconds.emit(elapsedTime.seconds)
##            self.setminutes.emit(elapsedTime.seconds/60)

    def stop(self):
        self._isRunning = False

    def start(self):
        super(StopwatchThread, self).start()
        self._isRunning = True

class GUI_Window(QtGui.QMainWindow, Ui_Window):
    def __init__(self, parent=None):
        super(GUI_Window, self).__init__(parent)
        self.setupUi(self)
        self.activateDial = True

        self.init_rpm_widget()

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
        
    def init_rpm_widget(self):
        self.dots = self.dots_widget.findChildren(QtGui.QLabel)
        
        for dot in self.dots:
            dot.setVisible(False)

        self.current_num_of_dots = 0
        self.scene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setSceneRect(0,0,self.graphicsView.frameSize().width(),self.graphicsView.frameSize().height())
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.updateLine(0)
    
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
            self.proc.start('python genrandomframes.py')
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
            #print lineunsplitted
            #print

            line =  lineunsplitted.split()
            
            self.framesLabel.setText(lineunsplitted)
            rpm = int(line[0], base=16)
            engine_temp = int(line[1], base=16)
            voltage = int(line[2], base=16)
            current = int(line[3], base=16)
        else: 
            rpm = 0
            engine_temp = 0
            voltage = 0
            current = 0
            
        if self.isActive:
            self.updateRPM(rpm)
            self.updateEngineTemp(engine_temp)
            self.updateVoltage(voltage)
            self.updateCurrent(current)

    def updateRPM(self, rpm):
        if self.activateDial:
            rpm = self.dial.value()

        number_of_dots = rpm/(MAX_RPM_VALUE/len(self.dots))
        
        if number_of_dots != self.current_num_of_dots:
            for dot in self.dots[:number_of_dots]:
                if not dot.isVisible():
                    dot.setVisible(True)
            for dot in self.dots[number_of_dots:]:
                if dot.isVisible():
                    dot.setVisible(False)
            self.rpmNumber.display(rpm)
        self.current_num_of_dots = number_of_dots

        self.updateLine(rpm)

    def updateLine(self, value):
        if self.activateDial:
            value = self.dial.value()
            
        self.scene.clear()

        pen = QtGui.QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap)

        x1 = self.graphicsView.width()/2
        y1 = self.graphicsView.height()/2

        line_length = self.graphicsView.width()/2 - 10
        angle = (math.radians(ANGLE_RANGE) * value)/255.0
        angle_offset = (360 - ANGLE_RANGE)/2
        x2 = line_length * math.sin(angle + math.radians(angle_offset))
        y2 = -1 * line_length * math.cos(angle + math.radians(angle_offset))

        #print line_length, '|', value, '|', math.degrees(angle), '|', x2, y2
        
        line = QtCore.QLineF(x1, y1 ,x1-x2,y1-y2)
        lineItem = QtGui.QGraphicsLineItem(line, scene=self.scene)
        lineItem.setPen(pen)

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
