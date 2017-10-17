# @autor: Karol Siegieda
import os
import sys
#import can
import subprocess
from PyQt4 import QtCore, QtGui
from src.modules.utils import *
import math
from src.gui.widgets import RPM_Widget
from src.modules.settings import *
from functools import partial
import random
from src.gui.MainWindow import Ui_MainWindow
#from src.gui.BmsWindow import Ui_Form


systemStatus = 0
s = 0
m = 0
ms = 0
timerStarted = False
lapTimesCounter = 0

##class GUI_BMSWindow(QtGui.QWidget, Ui_Form):
##    def __init__(self, parent=None):
##        super(GUI_BMSWindow, self).__init__(parent) # (, QtCore.Qt.FramelessWindowHint)
##        self.setupUi(self)
##        QtCore.QObject.connect(self.closeBmsWindow, QtCore.SIGNAL("clicked()"), self.closeWindow)
##
##    def closeWindow(self):
##        self.close()


class GUI_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI_MainWindow, self).__init__(parent) #, , QtCore.Qt.FramelessWindowHint
        self.connectionStatus = 0
        global systemStatus
        systemStatus = 0
        self.setupUi(self)
        self.gg = RPM_Widget(self.rpm_widget) #self.gg.updateRPM(100)
        self.proc = QtCore.QProcess()
        self.functionButtons()
        self.setConnectionStatus()
        self.laptimer = QtCore.QTimer(self)
        self.laptimer.timeout.connect(self.lapTimer)
        systemStatus = 1
        self.setSystemStatus()
        self.proc.readyReadStandardOutput.connect(partial(self.updateScreen, self.proc))

    def initialiseCAN(self):
        if self.connectionStatus == 0:
            try:
                system.os("sudo ip link set can0 up type can bitrate 250000")
                message = "CAN initialized. Bitrate = 250kh/s."
                self.writeConsoleMessage(message)
            except Exception:
                message = "CAN couldn't be initialised. Check configuration"
                systemStatus = 0
        self.setSystemStatus()
        self.proc.kill()
        self.proc.setProcessChannelMode(self.proc.MergedChannels)
        self.proc.start(TEST_COMMAND)
        self.connectionStatus = 1


    def updateScreen(self, proc):
        lineunsplitted = str(proc.readAllStandardOutput()).strip()
        line = lineunsplitted.split()
        if (line[1] == "0CF11E05"):
            rpm_lsb = int(line[3], base=16)
            rpm_msb = int(line[4], base=16)
            rpm_dec = rpm_msb * 256 + rpm_lsb
            self.gg.updateRPM(random.randrange(0,7000))


    def test(self):
        self.gg.updateRPM(random.randrange(0, 7000))

    def lapTimer(self):
        global s, m, ms
        if ms < 100:
            ms = ms + 1
        else:
            if s < 59:
                ms = 0
                s = s + 1
            elif s == 59 and m < 59:
                m = m + 1
                ms = 0
                s = 0
            else:
                self.laptimer.stop()
        self.time = "{0}:{1}:{2}".format(m, s, ms)
        self.lcdNumber.setDigitCount(len(self.time))
        self.lcdNumber.display(self.time)

    def startTimer(self):
        global s, m, ms
        global timerStarted
        global lapTimesCounter
        global systemStatus
        self.startLapTimer.setText('Start Lap Timer')
        try:
            if timerStarted is False:
                timerStarted = True
                self.startLapTimer.setStyleSheet('QPushButton {'
                    'border-image: url("img/start_lap_button_clicked.png");'
                    'font 75 italic 14 "Gill Sans MT";'
                    'color: rgb(216,216,216);}'
                )
                self.startLapTimer.setText('Stop Lap Timer')
                self.laptimer.start(10)
            elif timerStarted is True:
                self.sleepTimer = QtCore.QTimer()
                self.sleepTimer.setInterval(2500)
                self.sleepTimer.setSingleShot(True)
                self.sleepTimer.start()
                self.startLapTimer.setStyleSheet('QPushButton {'
                    'border-image: url("img/start_lap_button.png");'
                    'font 75 italic 14 "Gill Sans MT";'
                    'color: rgb(216,216,216);}')
                message = (' Stopping timer... \n     Transfering time: ' +
                           self.time + ' to \n     Lap Times Table')
                self.writeConsoleMessage(message)
                self.laptimer.stop()
                lapTimesCounter = lapTimesCounter + 1
                self.lapTimes.setRowCount(lapTimesCounter)
                self.lapTimes.setItem(lapTimesCounter - 1, 0, QtGui.QTableWidgetItem(str(m) +
                                      "m   " + str(s) + "s  " + str(ms * 10) + "ms"))
                self.lapTimes.scrollToBottom()
                s = 0
                m = 0
                ms = 0
                self.sleepTimer.timeout.connect(self.resetTimer)
                timerStarted = False
            else:
                message = 'Unknown Timer Error. Check log.'
                self.writeConsoleMessage(message)
                log = 'Unexpected timer condition value: ' + timerStarted
                print(log)

        except Exception:
            systemStatus = 0
            self.setSystemStatus()
            self.laptimer.stop()
            message = 'Lap Timer Error..Stopping service.'
            self.writeConsoleMessage(message)

    def writeConsoleMessage(self, message):
        self.console.append(self.systemTime() + message)

    def clearConsole(self):
        self.console.clear()

    def resetTimer(self):
        s = 0
        m = 0
        ms = 0
        self.time = "{0}:{1}:{2}".format(m, s, ms)
        self.lcdNumber.setDigitCount(len(self.time))
        self.lcdNumber.display(self.time)

    def functionButtons(self):
        QtCore.QObject.connect(self.closeApplication, QtCore.SIGNAL("clicked()"), self.test) #self.closeWindow
        QtCore.QObject.connect(self.closeApplication, QtCore.SIGNAL("pressed()"), self.startCloseTimer)
        QtCore.QObject.connect(self.batteryDetails, QtCore.SIGNAL("clicked()"), self.openBmsWindow)
        QtCore.QObject.connect(self.connectBMS, QtCore.SIGNAL("clicked()"), self.initialiseCAN)
        QtCore.QObject.connect(self.startLapTimer, QtCore.SIGNAL("clicked()"), self.startTimer)
        QtCore.QObject.connect(self.clearLapTimes, QtCore.SIGNAL("clicked()"), self.clearLapTable)
        QtCore.QObject.connect(self.clearAlerts, QtCore.SIGNAL("clicked()"), self.clearConsole)

    def clearLapTable(self):
        global lapTimesCounter
        self.lapTimes.setRowCount(0)
        lapTimesCounter = 0

    def startCloseTimer(self):
        self.singletimer = QtCore.QTimer()
        self.singletimer.singleShot(2000, self.shutdownSystem)

    def closeWindow(self):
        global systemStatus
        self.console.clear()
        message = ' Application is going to close now'
        self.writeConsoleMessage(message)
        try:
            self.close()
            self.bmsWindow.closeWindow()
        except Exception:
            systemStatus = 0
            self.setSystemStatus()
            message = 'An error occured during closing application.'
            self.writeConsoleMessage(message)

    def shutdownSystem(self):
        global systemStatus
        if self.closeApplication.isDown() is True:
            self.console.clear()
            try:
                message = ' SYSTEM IS GOING TO SHUTDOWN NOW'
                self.writeConsoleMessage(message)
                command = "/usr/bin/sudo /sbin/shutdown -r now"
                import subprocess
                process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
                output = process.communicate()[0]
                self.console.append(output)
                
            except Exception:
                systemStatus = 0
                self.setSystemStatus()
                message = 'An error occured during closing application.'
                self.writeConsoleMessage(message)

    def openBmsWindow(self):
        self.bmsWindow.setGeometry(1052, 250, 250, 408)
        self.bmsWindow.show()


    def systemTime(self):
        time = QtCore.QTime.currentTime()
        return(time.toString('hh:mm:ss' + ' : '))

    def setSystemStatus(self):
        if(systemStatus == 1):
            self.statusBar.setStyleSheet(
                " border-image: url('img/green-03.jpg');"
                " font: 75 italic 16pt 'Gill Sans MT' ; "
                " color: rgb(49, 51, 49); ")
            self.statusBar.setText("OK!")
        elif (systemStatus == 0):
            self.statusBar.setStyleSheet(
                " border-image: url('img/red-04.jpg');"
                " font: 75 italic 14pt 'Gill Sans MT' ; "
                " color: rgb(35, 44, 35); ")
            self.statusBar.setText("Error. Check Alerts")
        else:
            self.statusBar.setText("Unknown error.")

    def setConnectionStatus(self):
        if(self.connectionStatus == 1):
            self.connectionBar.setStyleSheet(
                " border-image: url('img/green-03.jpg');"
                " font: 75 italic 16pt 'Gill Sans MT' ; "
                " color: rgb(49, 51, 49); ")
            self.statusBar.setText("Connected")
        elif (self.connectionStatus == 0):
            self.connectionBar.setStyleSheet(
                " border-image: url('img/red-04.jpg');"
                " font: 75 italic 14pt 'Gill Sans MT' ; "
                " color: rgb(35, 44, 35); ")
            self.connectionBar.setText("Not connected")
        else:
            self.statusBar.setText("Unknown error.")

    def portOpen(self):
        try:
            self.port = serial.Serial("/dev/ttyUSB0", 9600)
            print("Serial port " + self.port.name + "opened")
        except SerialException as e:
            print("Could not open port")

    def ReadData(self):
        tablica_funkcji=np.zeros((16,2), float)
        for i in range(0, 16):
                print("Timer function")
                dane = self.port.read(2)
                window.Console_2.append(dane)
                dane = list(dane)
                dane1 = dane[0]
                dane1 = ord(dane1)
                dane2 = dane[1]
                dane2 = ord(dane2)
                funkcja = ((dane1 & 0xF0) >> 4)
                wartosc = ((dane1 & 0x0F) << 8) + dane2
                tablica_funkcji[i][0] = wartosc
                tablica_funkcji[i][1] = funkcja
                if (i == 15):
                        tablica2 = tablica_funkcji[tablica_funkcji[:, 1].argsort()]
                        SumVoltage = 0
                        Current = 0
                        for j in range(0, 13):
                            tablica2[j + 3][0] = ((tablica2[j + 3][0] * 4.0)/4096.0) + 1
                            SumVoltage = SumVoltage + tablica2[j + 3][0]
                        Current = (0.394 * tablica2[0][0] - 683.87)
                        window.voltageBar.setValue(SumVoltage)
                        window.currentBar.setValue(Current)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = GUI_MainWindow()
    window.show()
    app.exec_()
