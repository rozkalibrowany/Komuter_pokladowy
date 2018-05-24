from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from src.gui.newGui import Ui_MainWindow
from PyQt5.QtQml import qmlRegisterType
from src.gui.RadialBar import RadialBar
from src.modules.settings import *
import datetime

from src.gui.widgets import RPM_Widget
from PyQt5.QtCore import QProcess
from collections import deque
from functools import partial
from src.modules.settings import *
from src.modules.utils import *

s = 0
m = 0
ms = 0
timerStarted = False

class GUI_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI_MainWindow, self).__init__(parent)       #QtCore.Qt.FramelessWindowHint
        self.setupUi(self)
        qmlRegisterType(RadialBar, "SDK", 1,0, "RadialBar")

        self.gg = RPM_Widget(self.rpm_widget)
        self.proc = QProcess()
        self.gg.updateRPM(1355)
        self.proc.readyReadStandardOutput.connect(partial(self.updateData, self.proc))
        self.container_rpm = deque([], 4)
        self.container_current = deque([], 4)
        self.gg.rpmNumber.display(33)

        self.laptimer = QTimer(self)
        self.laptimer.timeout.connect(self.Timer)
        self.functionButtons()
        self.lastButtonObject = QtWidgets.QFrame()         # przechowuje obiekt poprzedniego przycisku menu
        self.objectList = []

        self.pageMap = {'vfMain': 0, 'vfAlerts': 1, 'vfStats': 2, 'vfSettings': 3}
        self.container_rpm = deque([], 4)
        self.container_current = deque([], 4)
        self.menuButtonChanged(self.vfMain)
        self.setConnectionStatus(True)
        self.setAlertStatus(False)
        self.setSystemTime()
        self.timerButton.setText('Start Timer')

    def updateData(self, proc):
        lineunsplitted = str(proc.readAllStandardOutput()).strip()
        line = lineunsplitted.split()[1:]
        line[-1] = line[-1].replace("\\r\\n'", '') if "\\r\\n'" in line[-1] else line[-1]
        print(line)
        line = line[1:2] + line [3:]
        ##### RPM ##################
        if (line[0] == "0CF11E05"):
            rpm_lsb = int(line[1], base=16)
            rpm_msb = int(line[2], base=16)
            rpm = rpm_msb * 256 + rpm_lsb
            self.container_rpm.append(rpm)
            avg = sum(self.container_rpm) / len(self.container_rpm)
            self.gg.updateRPM(avg)

    def initialiseCAN(self):
        #if self.connectionStatus == 0:
        #    try:
        #        system.os("sudo ip link set can0 up type can bitrate 250000")
        #        message = "CAN initialized. Bitrate = 250kh/s."
        #        self.writeConsoleMessage(message)
        #    except Exception:
        #        message = "CAN couldn't be initialised. Check configuration"
        #        systemStatus = 0
        self.proc.kill()
        self.proc.setProcessChannelMode(self.proc.MergedChannels)
        self.proc.start(TEST_COMMAND)

    def functionButtons(self):
        self.driveButton.pressed.connect(lambda: self.menuButtonChanged(self.vfMain))
        self.alertsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfAlerts))
        self.statsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfStats))
        self.settingsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfSettings))
        self.timerButton.clicked.connect(self.startTimer)
        self.timerButton.clicked.connect(self.initialiseCAN)

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
            self.canStatus.setText("Connected")
            self.canStatus.setProperty('connected', True)
            self.canStatus.style().unpolish(self.canStatus)
            self.canStatus.style().polish(self.canStatus)
            self.canStatus.update()
        else:
            self.canStatus.setText("Not connected")
            self.canStatus.setProperty('connected', False)
            self.canStatus.style().unpolish(self.canStatus)
            self.canStatus.style().polish(self.canStatus)
            self.canStatus.update()

    def setAlertStatus(self, isAlert):
        if (isAlert):
            self.alertStatus.setText("1 alert")
            self.alertStatus.setProperty('isAlert', True)
            self.alertStatus.style().unpolish(self.canStatus)
            self.alertStatus.style().polish(self.canStatus)
            self.alertStatus.update()
        else:
            self.alertStatus.setText("No alerts")
            self.alertStatus.setProperty('isAlert', False)
            self.alertStatus.style().unpolish(self.canStatus)
            self.alertStatus.style().polish(self.canStatus)
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