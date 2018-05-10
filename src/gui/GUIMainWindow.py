# -*- coding: utf-8 -*-
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QThreadPool
from src.modules.utils import *
import math
from src.gui.widgets import RPM_Widget
from src.modules.settings import *
from functools import partial
import random
from src.gui.MainWindow2 import Ui_MainWindow
from collections import deque
from src.modules.AlertsWindow import AlertsWindow

systemStatus = 0
s = 0
m = 0
ms = 0
timerStarted = False
lapTimesCounter = 0

class GUI_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI_MainWindow, self).__init__(parent, QtCore.Qt.FramelessWindowHint)

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
        self.container_rpm = deque([], 4)
        self.container_current = deque([], 4)
        self.alertsWindow = AlertsWindow()

    def initialiseCAN(self):
        #if self.connectionStatus == 0:
        #    try:
        #        system.os("sudo ip link set can0 up type can bitrate 250000")
        #        message = "CAN initialized. Bitrate = 250kh/s."
        #        self.writeConsoleMessage(message)
        #    except Exception:
        #        message = "CAN couldn't be initialised. Check configuration"
        #        systemStatus = 0
        self.setSystemStatus()
        self.proc.kill()
        self.proc.setProcessChannelMode(self.proc.MergedChannels)
        self.proc.start(TEST_COMMAND)
        self.connectionStatus = 1


    def updateScreen(self, proc):
        lineunsplitted = str(proc.readAllStandardOutput()).strip()
        line = lineunsplitted.split()[1:]
        line[-1] = line[-1].replace("\\r\\n'", '') if "\\r\\n'" in line[-1] else line[-1]
        print(line)
        line = line[1:2] + line [3:]
        print(line)
        ##### RPM ##################
        if (line[0] == "0CF11E05"):
            rpm_lsb = int(line[1], base=16)
            rpm_msb = int(line[2], base=16)
            rpm = rpm_msb * 256 + rpm_lsb
            self.container_rpm.append(rpm)
            avg = sum(self.container_rpm) / len(self.container_rpm)
            self.gg.updateRPM(avg)
        ##### CURRENT ###############
            current_lsb = int(line[3], base=16)
            current_msb = int(line[4], base=16)
            current = (current_msb * 256 + current_lsb) / 10
            self.container_current.append(current)
            avg = sum(self.container_current) / len(self.container_current)
            self.currentBar.setValue(avg)
        ##### VOLTAGE ####################
            voltage_lsb = int(line[5], base=16)
            voltage_msb = int(line[6], base=16)
            voltage = (voltage_msb * 256 + voltage_lsb) / 10
            self.voltageBar.setValue(voltage)
        ##### ERRORS #######################
            errors_lsb = '{:08b}'.format(int(line[7], base=16))
            errors_msb = '{:08b}'.format(int(line[8], base=16))

            ### random, for testing only:
            #k, m = random.randrange(0, len(errors_lsb)), random.randrange(0, len(errors_msb))
            #errors_lsb = errors_lsb[:k] + '1' + errors_lsb[k+1:]
            #errors_msb = errors_msb[:m] + '1' + errors_msb[m+1:]

            ### all green
            errors_lsb = '11111111'
            errors_msb = '11111111'

            for i, bit in enumerate((errors_msb + errors_lsb)[::-1]):
                if ERR[i] != 'RESERVED':
                    self.alertsWindow.leds['led_err'+str(i)].setChecked(bit == '1')
        else:
            throttle = int(line[1], base=16)
            throttle = throttle / 51
            self.throttleBar.setValue(throttle)
        #######################################3
            controller_temp = int(line[2], base=16)
            controller_temp = controller_temp - 40
            self.controllerTempBar.setValue(controller_temp)
        ########################################
            # motor_temp = int(line[3], base=16)
            motor_temp = controller_temp + 10
            self.motorTempBar.setValue(motor_temp)


    def test(self):
        self.thread.start()


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
        self.closeApplication.clicked.connect(self.closeWindow) #s
        self.closeApplication.pressed.connect(self.startCloseTimer)
        self.batteryDetails.clicked.connect(self.openBmsWindow)
        self.connectBMS.clicked.connect(self.initialiseCAN)
        self.startLapTimer.clicked.connect(self.startTimer)
        self.clearLapTimes.clicked.connect(self.clearLapTable)
        self.clearAlerts.clicked.connect(self.clearConsole)


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
        self.alertsWindow.close()
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
##        self.bmsWindow.setGeometry(1052, 250, 250, 408)
##        self.bmsWindow.show()
        if self.alertsWindow.isVisible():
            self.alertsWindow.close()
        else:
            self.alertsWindow.setGeometry(self.x(), self.y(), 330, 581)
            self.alertsWindow.show()


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

    def write():
        name ="can_data" +datetime.datetime.minutes()+"."+datetime.datetime.seconds()+".csv"
        write= -write
        if write:
            name ="can_data" +datetime.datetime.minutes()+"."+datetime.datetime.seconds()+".csv"
            if names==None:
                names[0]=name
                names[1]=name
            else:
                names[1]=names[0]
                names[0]=name