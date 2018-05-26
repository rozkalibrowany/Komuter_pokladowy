from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from src.gui.newGui import Ui_MainWindow
from src.modules.settings import *
import datetime

from src.gui.widgets import RPM_Widget
from PyQt5.QtCore import QProcess, Qt
from collections import deque
from functools import partial
from src.modules.settings import *
from src.modules.utils import *

from src.gui.LedIndicatorWidget import *
import re
s = 0
m = 0
ms = 0
timerStarted = False

class GUI_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI_MainWindow, self).__init__(parent, Qt.FramelessWindowHint)       #QtCore.Qt.FramelessWindowHint
        self.setupUi(self)
        #### Set resolution and center window ###
        self.setGeometry(0, 0, 800, 480)
        self.setWindowTitle("ADek GUI Window v0.1")
        self.centerOnScreen()
        ###########                      #########

        self.connected = False
        self.gg = RPM_Widget(self.rpm_widget)
        self.proc = QProcess()
        self.proc.readyReadStandardOutput.connect(partial(self.updateData, self.proc))

        ##########   Kontenery   #################
        self.containerRpm = deque([], 3)        # ile probek do obrotów
        self.containerCurrent = deque([], 6)    # ile próbek do prądu
        self.containerVoltage = deque([], 5)    # ile próbek napięcia
        self.containerPower = deque([], 5)    # ile próbek mocy
        ###########                      #########

        self.laptimer = QTimer(self)
        self.laptimer.timeout.connect(self.Timer)
        self.functionButtons()
        self.lastButtonObject = QtWidgets.QFrame()         # przechowuje obiekt poprzedniego przycisku menu
        self.objectList = []

        self.leds = {}
        self.Alerts()

        self.counter = 0
        self.pageMap = {'vfMain': 0, 'vfAlerts': 1, 'vfStats': 2, 'vfSettings': 3}
        self.menuButtonChanged(self.vfMain)
        self.setConnectionStatus(False)
        self.setAlertStatus(False, "")
        self.setSystemTime()
        self.timerButton.setText('Start Timer')

    def centerOnScreen (self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def updateData(self, proc):
        alertCounter = 0
        if (self.counter == 100):
            self.counter = 0     # wyzeruj licznik

        lineunsplitted = str(proc.readAllStandardOutput()).strip()
        line = lineunsplitted.split()[1:]
        line[-1] = line[-1].replace("\\r\\n'", '') if "\\r\\n'" in line[-1] else line[-1]
        #print(line)
        line = line[1:2] + line [3:]

        ##### RPM ##################
        if (line[0] == "0CF11E05"):
            rpm_lsb = int(line[1], base=16)
            rpm_msb = int(line[2], base=16)
            rpm = rpm_msb * 256 + rpm_lsb
            self.containerRpm.append(rpm)
            avg = sum(self.containerRpm) / len(self.containerRpm)
            self.gg.updateRPM(avg)

        ##### CURRENT ###############
            current_lsb = int(line[3], base=16)
            current_msb = int(line[4], base=16)
            current = (current_msb * 256 + current_lsb) / 10
            self.containerCurrent.append(current)
            avgCurrent = sum(self.containerCurrent) / len(self.containerCurrent)
            self.batteryCurrentLcd.display(int(avgCurrent))
            if (self.counter % 3 == 0):
                self.setLcdNumberStyle(self.batteryCurrentLcd, int(avgCurrent), 100, 160, True)
                self.setLcdNumberStyle(self.batteryCurrent, int(avgCurrent), 100,160, True)      # warning na 100A, warning2 na 160A

        ##### VOLTAGE ####################
            voltage_lsb = int(line[5], base=16)
            voltage_msb = int(line[6], base=16)
            voltage = (voltage_msb * 256 + voltage_lsb) / 10
            self.containerVoltage.append(voltage)
            avgVoltage = sum(self.containerVoltage) / len(self.containerVoltage)
            self.batteryVoltageLcd.display(avgVoltage)
            if (self.counter % 3 == 0):
                self.setLcdNumberStyle(self.batteryVoltageLcd, int(avgVoltage), 86.4, 74, False)
                self.setLcdNumberStyle(self.batteryVoltage, int(avgVoltage), 86.4, 74, False)     # po 3.6V na celę , warning2 po 3.1V na celę

        ##### POWER ####################
            power = avgCurrent * avgVoltage
            self.containerPower.append(power)
            avgPower = sum(self.containerPower) / len(self.containerPower)
            avgPower = int(avgPower)/1000
            self.avrPowerLcd.display(avgPower)
            if (self.counter % 3 == 0):
                self.setLcdNumberStyle(self.avrPowerLcd, int(avgPower), 10, 25, True)
                self.setLcdNumberStyle(self.avrPower, int(avgPower), 10, 25, True)     # warning na 10kW, warning2 na 25kW

        ##### ERRORS #######################
            line[8] = line[8].replace("\\n'", "")
            line[8] = '0x1D'
            line[7] = '0x1D'
            errors_lsb = '{:08b}'.format(int(line[7], base=16))
            errors_msb = '{:08b}'.format(int(line[8], base=16))

            for i, bit in enumerate((errors_msb + errors_lsb)[::-1]):
                if ERR[i] != 'RESERVED':
                    self.leds['led_err'+str(i)].setChecked(bit == '1')
                    self.leds['led_err'+str(i)].setDown(bit == '1')
                    if (self.leds['led_err'+str(i)].isDown() == True):
                        alertCounter = alertCounter + 1
            if (alertCounter > 0 and self.counter % 5 == 0):
                self.setAlertStatus(True, alertCounter)
                self.setAlertButtonInAlarm(True)
            else:
                self.setAlertButtonInAlarm(False)

        else:
        ##### THROTTLE ####################
            throttle = int(line[1], base=16)
            throttle = throttle / 2.55
            self.throttleLcd.display(int(throttle))

        ##### CONTROLLER ##################
            contrTemp = int(line[2], base=16)
            contrTemp = contrTemp - 40
            self.contrTempLcd.display(contrTemp)
            if (self.counter % 3 == 0):
                self.setLcdNumberStyle(self.contrTempLcd, int(contrTemp), 45, 65, True)
                self.setLcdNumberStyle(self.contrTemp, int(contrTemp), 45, 65, True)

        ##### MOTOR TEMP #######################
            motorTemp = int(line[3], base=16)
            motorTemp = motorTemp - 30
            self.motorTempLcd.display(motorTemp)
            if (self.counter % 3 == 0):
                self.setLcdNumberStyle(self.motorTempLcd, int(motorTemp), 50, 65, True)
                self.setLcdNumberStyle(self.motorTemp, int(motorTemp), 50, 65, True)
        self.counter = self.counter + 1

    def setAlertButtonInAlarm(self, isAlert):
        if (isAlert):
            self.vfAlerts.setProperty('alert', True)
            self.vfAlerts.style().unpolish(self.vfAlerts)
            self.vfAlerts.style().polish(self.vfAlerts)
            self.vfAlerts.update()
        else:
            self.vfAlerts.setProperty('alert', False)
            self.vfAlerts.style().unpolish(self.vfAlerts)
            self.vfAlerts.style().polish(self.vfAlerts)
            self.vfAlerts.update()

    def setLcdNumberStyle(self, widget, avg, limitValue, limitValue2, setTrue):
        if (avg > limitValue2):
            widget.setProperty('warning2', setTrue)
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()
        elif (avg > limitValue):
            widget.setProperty('warning', setTrue)
            widget.setProperty('warning2', not setTrue)
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()
        else:
            widget.setProperty('warning', not setTrue)
            widget.setProperty('warning2', not setTrue)
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()

    def Alerts(self):
        led_slots = self.findChildren(QtWidgets.QFrame)
        for led_slot in led_slots:
            if re.match('led_err', led_slot.objectName()):
                l = LedIndicator(led_slot)
                l.setGeometry(0,0,30,30)
                self.leds[str(led_slot.objectName())] = l
            elif re.match('label_err', led_slot.objectName()):
                number = str(led_slot.objectName()).replace('label_err', '')
                led_slot.setText(ERR[int(number)])

    def initialiseCAN(self):
        #if self.connectionStatus == 0:
        #    try:
        #        system.os("sudo ip link set can0 up type can bitrate 250000")
        #        message = "CAN initialized. Bitrate = 250kh/s."
        #        self.writeConsoleMessage(message)
        #    except Exception:
        #        message = "CAN couldn't be initialised. Check configuration"
        #        systemStatus = 0
        try:
            self.proc.kill()
            self.proc.setProcessChannelMode(self.proc.MergedChannels)
            self.proc.start(TEST_COMMAND)
            if (self.connected):
                self.setConnectionStatus(False)
                self.connected = False
            else:
                self.setConnectionStatus(True)
                self.connected = True
        except Exception as e:
            print("CAN connection error!")
            self.setConnectionStatus(False)

    def functionButtons(self):
        self.driveButton.pressed.connect(lambda: self.menuButtonChanged(self.vfMain))
        self.alertsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfAlerts))
        self.statsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfStats))
        self.settingsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfSettings))
        self.timerButton.clicked.connect(self.startTimer)
        self.canButton.clicked.connect(self.initialiseCAN)

    def menuButtonChanged(self, widget):
        self.objectList.append(widget)
        iconObject = widget.findChild(QtWidgets.QPushButton)
        self.objectList.append(iconObject)
        textObject = widget.findChild(QtWidgets.QLabel)
        self.objectList.append(textObject)
        objectListCopy = self.objectList

        if not self.lastButtonObject.objectName():
            self.lastButtonObject = widget
            self.setNewPage(self.pageMap[widget.objectName()])         # zmien stronę
            self.menuButtonAreaStyleUpdate(objectListCopy, True)
        else:
            if self.lastButtonObject.objectName() != widget.objectName():
                self.setNewPage(self.pageMap[widget.objectName()])     # zmien stronę
                self.menuButtonAreaStyleUpdate(objectListCopy, True)
                del self.objectList[:]              # wyczyszczenie listy obiektów

                self.objectList.append(self.lastButtonObject)
                oldIconObject = self.lastButtonObject.findChild(QtWidgets.QPushButton)
                self.objectList.append(oldIconObject)
                oldTextObject = self.lastButtonObject.findChild(QtWidgets.QLabel)
                self.objectList.append(oldTextObject)
                objectListCopy = self.objectList

                self.menuButtonAreaStyleUpdate(objectListCopy, False)
                del self.objectList[:]              # wyczyszczenie listy obiektów
                self.lastButtonObject = widget

    def menuButtonAreaStyleUpdate(self, objectList, ischanged):
        for widget in objectList:
            widget.setProperty('chosen', ischanged)
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()

    def setConnectionStatus(self, isConnected):
        if (isConnected):
            self.canButton.setText("Connected")
            self.canButton.setProperty('connected', True)
            self.canButton.style().unpolish(self.canButton)
            self.canButton.style().polish(self.canButton)
            self.canButton.update()
        else:
            self.canButton.setText("CAN Connect")
            self.canButton.setProperty('connected', False)
            self.canButton.style().unpolish(self.canButton)
            self.canButton.style().polish(self.canButton)
            self.canButton.update()

    def setAlertStatus(self, isAlert, alarmNr):
        if (isAlert):
            alert = str(alarmNr) + " Alerts!"
            self.alertStatus.setText(alert)
            self.alertStatus.setProperty('isAlert', True)
            self.alertStatus.style().unpolish(self.alertStatus)
            self.alertStatus.style().polish(self.alertStatus)
            self.alertStatus.update()
        else:
            self.alertStatus.setText("No alerts")
            self.alertStatus.setProperty('isAlert', False)
            self.alertStatus.style().unpolish(self.alertStatus)
            self.alertStatus.style().polish(self.alertStatus)
            self.alertStatus.update()

    def setSystemTime(self):
        now = datetime.datetime.now()
        self.timeLabel.setText(now.strftime("%H:%M"))
        self.dateLabel.setText(now.strftime("%Y-%m-%d"))

    def setNewPage(self, index):
        self.stackedWidget.setCurrentIndex(index)    # ustaw stronę


    def Timer(self):
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
        if timerStarted is False:
            timerStarted = True
            self.timerButton.setProperty('clicked', True)
            self.timerButton.style().unpolish(self.timerButton)
            self.timerButton.style().polish(self.timerButton)
            self.timerButton.update()
            self.timerButton.setText('Stop Timer')
            self.laptimer.start(10)
        elif timerStarted is True:
            self.sleepTimer = QTimer()
            self.sleepTimer.setInterval(2500)
            self.sleepTimer.setSingleShot(True)
            self.timerButton.setProperty('clicked', False)
            self.timerButton.style().unpolish(self.timerButton)
            self.timerButton.style().polish(self.timerButton)
            self.timerButton.update()
            self.timerButton.setText('Start Timer')
            self.sleepTimer.start()
            self.laptimer.stop()
            s = 0
            m = 0
            ms = 0
            self.sleepTimer.timeout.connect(self.resetTimer)
            timerStarted = False
        else:
            message = 'Unknown Timer Error. Check log.'
            print(message)

    def resetTimer(self):
        s = 0
        m = 0
        ms = 0
        self.time = "{0}:{1}:{2}".format(m, s, ms)
        self.lcdNumber.setDigitCount(len(self.time))
        self.lcdNumber.display(self.time)