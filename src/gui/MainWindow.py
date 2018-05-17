from PyQt5 import QtWidgets
from src.gui.newGui import Ui_MainWindow
clicked = False
lastButton = ""
changeButton = False


class GUI_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI_MainWindow, self).__init__(parent) #QtCore.Qt.FramelessWindowHint
        self.setupUi(self)
        self.functionButtons()
        self.lastButtonObject = QtWidgets.QFrame()

        #lastButtonObject = ""
    def functionButtons(self):
        self.driveButton.pressed.connect(lambda: self.menuButtonChanged(self.vfMain))
        self.alertsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfAlerts))
        self.statsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfStats))
        self.settingsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfSettings))

    def menuButtonChanged(self, widget):
        global lastButton
        global changeButton
        iconObject = widget.findChild(QtWidgets.QPushButton)
        textObject = widget.findChild(QtWidgets.QLabel)

        if not self.lastButtonObject.objectName():
            self.lastButtonObject = widget
            changeButton = True
        else:
            if self.lastButtonObject.objectName() != widget.objectName():
                self.menuButtonAreaStyleUpdate(self.lastButtonObject, False)
                oldIconObject = self.lastButtonObject.findChild(QtWidgets.QPushButton)
                oldTextObject = self.lastButtonObject.findChild(QtWidgets.QLabel)
                self.menuButtonAreaStyleUpdate(self.lastButtonObject, False)
                self.menuButtonAreaStyleUpdate(oldIconObject, False)
                self.menuButtonAreaStyleUpdate(oldTextObject, False)
                self.lastButtonObject = widget
                changeButton = True
            else:
                changeButton = False

        if changeButton == True:
            self.menuButtonAreaStyleUpdate(widget, True)
            self.menuButtonAreaStyleUpdate(iconObject, True)
            self.menuButtonAreaStyleUpdate(textObject, True)

    def menuButtonAreaStyleUpdate(self, widget, ischanged):
        widget.setProperty('chosen', ischanged)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()
