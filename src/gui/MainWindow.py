from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from src.gui.newGui import Ui_MainWindow
from PyQt5.QtQml import qmlRegisterType
from src.gui.RadialBar import *
from src.modules.settings import *
import datetime

from PyQt5.QtWidgets import QAbstractButton
from src.gui.widgets import RPM_Widget
from PyQt5.QtCore import QProcess, Qt
from collections import deque
from functools import partial
from src.modules.settings import *
from src.modules.utils import *

from src.gui.LedIndicatorWidget import *
import re
import random
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

        #########################################
        qmlRegisterType(RadialBar, "SDK", 1,0, "RadialBar")
        self.connected = False
        self.gg = RPM_Widget(self.rpm_widget)
        self.proc = QProcess()
        self.proc.readyReadStandardOutput.connect(partial(self.updateData, self.proc))
        self.container_rpm = deque([], 4)        # ile probek do obrotów
        self.container_current = deque([], 4)    # ile próbek do prądu

        self.laptimer = QTimer(self)
        self.laptimer.timeout.connect(self.Timer)
        self.functionButtons()
        self.lastButtonObject = QtWidgets.QFrame()         # przechowuje obiekt poprzedniego przycisku menu
        self.objectList = []

        self.leds = {}
        self.Alerts()

        self.pageMap = {'vfMain': 0, 'vfAlerts': 1, 'vfStats': 2, 'vfSettings': 3}
        self.container_rpm = deque([], 4)
        self.container_current = deque([], 4)
        self.menuButtonChanged(self.vfMain)
        self.setConnectionStatus(False)
        self.setAlertStatus(False, "")
        self.setSystemTime()
        self.timerButton.setText('Start Timer')

        self.batteryCurrentWidget = BatteryCurrentWidget()
        context = self.batteryCWidget.rootContext()
        context.setContextProperty("batteryCurrentWidget", self.batteryCurrentWidget)
        self.batteryCWidget.setSource(QUrl.fromLocalFile('src/gui/batteryCurrentRadialBar.qml'))

        self.batteryVoltageWidget = BatteryVoltageWidget()
        context = self.batteryVWidget.rootContext()
        context.setContextProperty("batteryVoltageWidget",self.batteryVoltageWidget)
        self.batteryVWidget.setSource(QUrl.fromLocalFile('src/gui/batteryVoltageRadialBar.qml'))

        self.batteryTempWidget = BatteryTempWidget()
        context = self.batteryTWidget.rootContext()
        context.setContextProperty("batteryTempWidget",self.batteryTempWidget)
        self.batteryTWidget.setSource(QUrl.fromLocalFile('src/gui/batteryTempRadialBar.qml'))

        self.contrTempWidget = ContrTempWidget()
        context = self.contrTWidget.rootContext()
        context.setContextProperty("contrTempWidget",self.contrTempWidget)
        self.contrTWidget.setSource(QUrl.fromLocalFile('src/gui/contrTempRadialBar.qml'))

        self.avrPowerWidget = AvrPowerWidget()
        context = self.avrPower.rootContext()
        context.setContextProperty("avrPowerWidget",self.avrPowerWidget)
        self.avrPower.setSource(QUrl.fromLocalFile('src/gui/avrPowerRadialBar.qml'))

        self.throttleWidget = ThrottleWidget()
        context = self.throttle.rootContext()
        context.setContextProperty("throttleWidget",self.throttleWidget)
        self.throttle.setSource(QUrl.fromLocalFile('src/gui/throttleRadialBar.qml'))

    def centerOnScreen (self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def updateData(self, proc):
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
            self.container_rpm.append(rpm)
            avg = sum(self.container_rpm) / len(self.container_rpm)
            self.gg.updateRPM(avg)

        ##### CURRENT ###############
            current_lsb = int(line[3], base=16)
            current_msb = int(line[4], base=16)
            current = (current_msb * 256 + current_lsb) / 10
            self.container_current.append(current)
            avgCurrent = sum(self.container_current) / len(self.container_current)
            self.batteryCurrentWidget.setValue(int(avgCurrent))

        ##### VOLTAGE ####################
            voltage_lsb = int(line[5], base=16)
            voltage_msb = int(line[6], base=16)
            avgVoltage = (voltage_msb * 256 + voltage_lsb) / 10
            self.batteryVoltageWidget.setValue(int(avgVoltage))

        ##### POWER ####################
            avrPower = avgCurrent * avgVoltage
            self.avrPowerWidget.setValue(int(avrPower)/1000)

        ##### ERRORS #######################
            line[8] = line[8].replace("\\n'", "")
            errors_lsb = '{:08b}'.format(int(line[7], base=16))
            errors_msb = '{:08b}'.format(int(line[8], base=16))

            for i, bit in enumerate((errors_msb + errors_lsb)[::-1]):
                if ERR[i] != 'RESERVED':
                    self.leds['led_err'+str(i)].setChecked(bit == '1')
                    self.leds['led_err'+str(i)].setDown(bit == '1')
                    if (self.leds['led_err'+str(i)].isDown() == True):
                        self.setAlertStatus(True, i)

        else:
        ##### THROTTLE ####################
            throttle = int(line[1], base=16)
            throttle = throttle / 2.55
            self.throttleWidget.setValue(int(throttle))

        ##### CONTROLLER ##################
            contrTemp = int(line[2], base=16)
            contrTemp = contrTemp - 40
            self.contrTempWidget.setValue(int(contrTemp))

        ##### MOTOR TEMP #######################
            motorTemp = int(line[3], base=16)
            motorTemp = motorTemp - 30
            self.batteryTempWidget.setValue(int(motorTemp))

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
                print(widget.objectName())
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
            alert = "ALERT NR " + str(alarmNr)
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