from PyQt5 import QtWidgets
from src.gui.newGui import Ui_MainWindow
clicked = False



class GUI_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI_MainWindow, self).__init__(parent) #QtCore.Qt.FramelessWindowHint
        self.setupUi(self)
        self.functionButtons()
        self.lastButtonObject = QtWidgets.QFrame() # przechowuje obiekt poprzedniego przycisku menu
        self.objectList = []


    def functionButtons(self):
        self.driveButton.pressed.connect(lambda: self.menuButtonChanged(self.vfMain))
        self.alertsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfAlerts))
        self.statsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfStats))
        self.settingsButton.pressed.connect(lambda: self.menuButtonChanged(self.vfSettings))


    def menuButtonChanged(self, widget):
        self.objectList.append(widget)
        iconObject = widget.findChild(QtWidgets.QPushButton)
        self.objectList.append(iconObject)
        textObject = widget.findChild(QtWidgets.QLabel)
        self.objectList.append(textObject)
        objectListCopy = self.objectList

        if not self.lastButtonObject.objectName():
            self.lastButtonObject = widget
            self.menuButtonAreaStyleUpdate(objectListCopy, True)
        else:
            if self.lastButtonObject.objectName() != widget.objectName():
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

