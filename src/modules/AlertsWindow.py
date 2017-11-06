from PyQt4 import QtCore, QtGui
from ..gui.alerts import Ui_Form as AlertsUI
from ..gui.LedIndicatorWidget import *
from ..modules.settings import *

class AlertsWindow(QtGui.QWidget, AlertsUI):
    def __init__(self, parent=None):
        super(AlertsWindow, self).__init__(parent, QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        led_slots = self.findChildren(QtGui.QFrame)
        self.leds = {}
        for led_slot in led_slots:
            if QtGui.QFrame == led_slot.__class__:
                l = LedIndicator(led_slot)
                l.setGeometry(0,0,30,30)
                self.leds[str(led_slot.objectName())] = l
            if QtGui.QLabel == led_slot.__class__:
                number = str(led_slot.objectName()).replace('label_err', '')
                led_slot.setText(ERR[int(number)])
        self.close_btn.clicked.connect(self.close)