# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/black_window_test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1016, 634)
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks|QtGui.QMainWindow.VerticalTabs)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("border-image: url(\"img/tlo.png\");"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 60, 291, 501))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(_fromUtf8("border-image: url(\"img/transparent.png\");"))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.batteryTempBar = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryTempBar.sizePolicy().hasHeightForWidth())
        self.batteryTempBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.batteryTempBar.setFont(font)
        self.batteryTempBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font: 75 italic 24pt \"Gill Sans MT\" ;\n"
"    color: rgb(24, 112, 194);\n"
"border-image: url(\"img/gradient3.png\");}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #FFFF00;\n"
"    border: 0,6px solid grey;\n"
"    border-radius: 4px;\n"
"    width: 8px;\n"
"    margin:1px;\n"
"\n"
"}\n"
""))
        self.batteryTempBar.setMaximum(75)
        self.batteryTempBar.setProperty("value", 23)
        self.batteryTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.batteryTempBar.setObjectName(_fromUtf8("batteryTempBar"))
        self.gridLayout_2.addWidget(self.batteryTempBar, 2, 1, 1, 1)
        self.voltageBar = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voltageBar.sizePolicy().hasHeightForWidth())
        self.voltageBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.voltageBar.setFont(font)
        self.voltageBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.voltageBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"border-image: url(\"img/gradient3.png\");    border: 3px solid white;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"font: 75 italic 24pt \"Gill Sans MT\" ;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(0, 175, 0);\n"
"    border: 0,6px solid grey;\n"
"    border-radius: 4px;\n"
"    width: 8px;\n"
"    margin:1px;\n"
"\n"
"\n"
"}\n"
""))
        self.voltageBar.setMaximum(60)
        self.voltageBar.setProperty("value", 30)
        self.voltageBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voltageBar.setInvertedAppearance(False)
        self.voltageBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.voltageBar.setObjectName(_fromUtf8("voltageBar"))
        self.gridLayout_2.addWidget(self.voltageBar, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");font: 75 italic 18pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.currentBar = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentBar.sizePolicy().hasHeightForWidth())
        self.currentBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.currentBar.setFont(font)
        self.currentBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"font: 75 italic 24pt \"Gill Sans MT\" ;\n"
"    color: rgb(255, 255, 255);\n"
"border-image: url(\"img/gradient3.png\");}\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color:rgb(232, 77, 0) ;\n"
"    border: 0,6px solid grey;\n"
"    border-radius: 4px;\n"
"    width: 8px;\n"
"    margin:1px;\n"
"\n"
"}\n"
""))
        self.currentBar.setMaximum(250)
        self.currentBar.setProperty("value", 100)
        self.currentBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentBar.setObjectName(_fromUtf8("currentBar"))
        self.gridLayout_2.addWidget(self.currentBar, 1, 1, 1, 1)
        self.engineTempBar = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engineTempBar.sizePolicy().hasHeightForWidth())
        self.engineTempBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.engineTempBar.setFont(font)
        self.engineTempBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font: 75 italic 24pt \"Gill Sans MT\" ;\n"
"    color: rgb(24, 112, 194);\n"
"border-image: url(\"img/gradient3.png\");}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #FFFF00;\n"
"    border: 0,6px solid grey;\n"
"    border-radius: 4px;\n"
"    width: 8px;\n"
"    margin:1px;\n"
"\n"
"}"))
        self.engineTempBar.setMaximum(75)
        self.engineTempBar.setProperty("value", 30)
        self.engineTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.engineTempBar.setObjectName(_fromUtf8("engineTempBar"))
        self.gridLayout_2.addWidget(self.engineTempBar, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");font: 75 italic 18pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.engineSpeedBar = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engineSpeedBar.sizePolicy().hasHeightForWidth())
        self.engineSpeedBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.engineSpeedBar.setFont(font)
        self.engineSpeedBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"    color: rgb(255, 255, 255);\n"
"border-image: url(\"img/gradient3.png\");}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(0, 68, 204);\n"
"    border: 0,6px solid grey;\n"
"    border-radius: 4px;\n"
"    width: 8px;\n"
"    margin:1px;\n"
"\n"
"}"))
        self.engineSpeedBar.setMaximum(5000)
        self.engineSpeedBar.setProperty("value", 1500)
        self.engineSpeedBar.setAlignment(QtCore.Qt.AlignCenter)
        self.engineSpeedBar.setObjectName(_fromUtf8("engineSpeedBar"))
        self.gridLayout_2.addWidget(self.engineSpeedBar, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 18pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.label_2.setLineWidth(3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 18pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.batteryTempBar.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.engineTempBar.raise_()
        self.engineSpeedBar.raise_()
        self.label_3.raise_()
        self.currentBar.raise_()
        self.voltageBar.raise_()
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(640, 1, 381, 581))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(_fromUtf8("\n"
"border-radius: 10px;\n"
"border-image: url(\"img/transparent.png\");"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.closeApplication = QtGui.QPushButton(self.frame_2)
        self.closeApplication.setGeometry(QtCore.QRect(180, 20, 161, 51))
        self.closeApplication.setStyleSheet(_fromUtf8("QPushButton {border-image: url(\"img/exit_button.png\");\n"
"font: 75 italic 20pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/exit_button_clicked.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}"))
        self.closeApplication.setText(_fromUtf8(""))
        self.closeApplication.setAutoRepeatDelay(2500)
        self.closeApplication.setAutoRepeatInterval(2100)
        self.closeApplication.setObjectName(_fromUtf8("closeApplication"))
        self.batteryDetails = QtGui.QPushButton(self.frame_2)
        self.batteryDetails.setGeometry(QtCore.QRect(180, 200, 161, 51))
        self.batteryDetails.setStyleSheet(_fromUtf8("QPushButton {border-image: url(\"img/battery_details_button.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/battery_details_button_clicked.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}"))
        self.batteryDetails.setText(_fromUtf8(""))
        self.batteryDetails.setObjectName(_fromUtf8("batteryDetails"))
        self.virtKeyboard = QtGui.QPushButton(self.frame_2)
        self.virtKeyboard.setGeometry(QtCore.QRect(180, 140, 161, 51))
        self.virtKeyboard.setStyleSheet(_fromUtf8("QPushButton {border-image: url(\"img/keyboard_button.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/keyboard_button_clicked.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}"))
        self.virtKeyboard.setText(_fromUtf8(""))
        self.virtKeyboard.setObjectName(_fromUtf8("virtKeyboard"))
        self.connectBMS = QtGui.QPushButton(self.frame_2)
        self.connectBMS.setGeometry(QtCore.QRect(180, 80, 161, 51))
        self.connectBMS.setStyleSheet(_fromUtf8("QPushButton {border-image: url(\"img/bms_connect_button.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/bms_connect_button_clicked.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}"))
        self.connectBMS.setText(_fromUtf8(""))
        self.connectBMS.setObjectName(_fromUtf8("connectBMS"))
        self.gridLayoutWidget = QtGui.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 340, 301, 201))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(-1, 15, -1, 25)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.adekLogo = QtGui.QLabel(self.gridLayoutWidget)
        self.adekLogo.setStyleSheet(_fromUtf8("border-image: url(\"img/adek3.png\");"))
        self.adekLogo.setText(_fromUtf8(""))
        self.adekLogo.setObjectName(_fromUtf8("adekLogo"))
        self.gridLayout_3.addWidget(self.adekLogo, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(0, 150, 341, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabWidget = QtGui.QTabWidget(self.frame_2)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 161, 271))
        self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget { /* The tab widget frame */\n"
"    border-top: 3px solid #C2C7CB;\n"
"border-image: url(\"img/gradient3.png\");\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 8px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 3px; /* move to the right by 5px */\n"
"border-image: url(\"img/gradient3.png\");\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 3px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 6px;\n"
"    min-width: 12ex;\n"
"    padding: 4px;\n"
"border-image: url(\"img/gradient3.png\");\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"border-image: url(\"img/gradient3.png\");\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: white; /* same as pane color */\n"
"border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 10pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 10pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}"))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lapTimes = QtGui.QTableWidget(self.tab)
        self.lapTimes.setGeometry(QtCore.QRect(0, 0, 161, 239))
        self.lapTimes.setMinimumSize(QtCore.QSize(26, 0))
        self.lapTimes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lapTimes.setStyleSheet(_fromUtf8("QTableWidget {\n"
"border-image: url(\"img/tlo.png\");\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 2ex;\n"
"    padding: 1px;\n"
"font: 75 italic 13pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"    border-image: url(\"img/gradient3.png\");\n"
"    padding: 1px;\n"
"    font-size: 11pt;\n"
"    border-style: none;\n"
"    border-bottom: 0.5px solid #fffff8;\n"
"    border-right: 2px solid #fffff8;\n"
"font: 75 10.5pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QHeaderView {border-image: url(\"img/tlo.png\")\n"
"\n"
";}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}\n"
"\n"
"QTableCornerButton::section {border-image: url(\"img/tlo.png\");}"))
        self.lapTimes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lapTimes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lapTimes.setAutoScrollMargin(10)
        self.lapTimes.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.lapTimes.setRowCount(0)
        self.lapTimes.setColumnCount(1)
        self.lapTimes.setObjectName(_fromUtf8("lapTimes"))
        item = QtGui.QTableWidgetItem()
        self.lapTimes.setHorizontalHeaderItem(0, item)
        self.lapTimes.horizontalHeader().setCascadingSectionResizes(False)
        self.lapTimes.horizontalHeader().setDefaultSectionSize(138)
        self.lapTimes.horizontalHeader().setMinimumSectionSize(29)
        self.lapTimes.verticalHeader().setDefaultSectionSize(30)
        self.lapTimes.verticalHeader().setSortIndicatorShown(False)
        self.lapTimes.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.bestLapTimes = QtGui.QTableWidget(self.tab_2)
        self.bestLapTimes.setGeometry(QtCore.QRect(0, 0, 161, 241))
        self.bestLapTimes.setStyleSheet(_fromUtf8("QTableWidget {\n"
"border-image: url(\"img/tlo.png\");\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 2ex;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"    border-image: url(\"img/gradient3.png\");\n"
"    padding: 1px;\n"
"    font-size: 11pt;\n"
"    border-style: none;\n"
"    border-bottom: 0.5px solid #fffff8;\n"
"    border-right: 2px solid #fffff8;\n"
"font: 75 italic 11pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QHeaderView {border-image: url(\"img/tlo.png\")\n"
"\n"
";}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}\n"
"\n"
"QTableCornerButton::section {border-image: url(\"img/tlo.png\");}"))
        self.bestLapTimes.setObjectName(_fromUtf8("bestLapTimes"))
        self.bestLapTimes.setColumnCount(1)
        self.bestLapTimes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.bestLapTimes.setHorizontalHeaderItem(0, item)
        self.bestLapTimes.horizontalHeader().setDefaultSectionSize(144)
        self.bestLapTimes.horizontalHeader().setMinimumSectionSize(29)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.clearLapTimes = QtGui.QPushButton(self.frame_2)
        self.clearLapTimes.setGeometry(QtCore.QRect(180, 260, 161, 51))
        self.clearLapTimes.setStyleSheet(_fromUtf8("QPushButton {border-image: url(\"img/clear_table.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/clear_table_clicked.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}"))
        self.clearLapTimes.setText(_fromUtf8(""))
        self.clearLapTimes.setObjectName(_fromUtf8("clearLapTimes"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 0, 301, 121))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.startLapTimer = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startLapTimer.sizePolicy().hasHeightForWidth())
        self.startLapTimer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.startLapTimer.setFont(font)
        self.startLapTimer.setStyleSheet(_fromUtf8("QPushButton {border-image: url(\"img/start_lap_button.png\");\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);}\n"
"\n"
"QPushButton:pressed {border-image: url(\"img/start_lap_button_clicked.png\");\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216)\n"
"}"))
        self.startLapTimer.setObjectName(_fromUtf8("startLapTimer"))
        self.verticalLayout_2.addWidget(self.startLapTimer)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.lcdNumber = QtGui.QLCDNumber(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setSizeIncrement(QtCore.QSize(7, 21))
        self.lcdNumber.setBaseSize(QtCore.QSize(13, 0))
        self.lcdNumber.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber.setLineWidth(4)
        self.lcdNumber.setMidLineWidth(10)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 141, 23))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 0, 141, 23))
        self.pushButton_3.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.statusBar = QtGui.QPushButton(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(180, 0, 141, 23))
        self.statusBar.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.statusBar.setText(_fromUtf8(""))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.connectionBar = QtGui.QPushButton(self.centralwidget)
        self.connectionBar.setGeometry(QtCore.QRect(180, 30, 141, 23))
        self.connectionBar.setStyleSheet(_fromUtf8("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.connectionBar.setText(_fromUtf8(""))
        self.connectionBar.setObjectName(_fromUtf8("connectionBar"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(320, 0, 3, 582))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.clearAlerts = QtGui.QPushButton(self.centralwidget)
        self.clearAlerts.setGeometry(QtCore.QRect(330, 550, 301, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearAlerts.sizePolicy().hasHeightForWidth())
        self.clearAlerts.setSizePolicy(sizePolicy)
        self.clearAlerts.setMinimumSize(QtCore.QSize(256, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.clearAlerts.setFont(font)
        self.clearAlerts.setStyleSheet(_fromUtf8("QPushButton {border-image: url(\"img/start_lap_button.png\");\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);}\n"
"\n"
"QPushButton:pressed {border-image: url(\"img/start_lap_button_clicked.png\");\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216)\n"
"}"))
        self.clearAlerts.setObjectName(_fromUtf8("clearAlerts"))
        self.console = QtGui.QTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(330, 420, 301, 131))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMinimumSize(QtCore.QSize(0, 0))
        self.console.setMaximumSize(QtCore.QSize(16777215, 380))
        self.console.setStyleSheet(_fromUtf8("font: 75 italic 11pt;\n"
"border: 5px solid grey;\n"
"border-radius: 10px;\n"
"color: rgb(216, 216, 216);"))
        self.console.setAutoFormatting(QtGui.QTextEdit.AutoNone)
        self.console.setTabStopWidth(73)
        self.console.setObjectName(_fromUtf8("console"))
        self.rpm_widget = QtGui.QWidget(self.centralwidget)
        self.rpm_widget.setGeometry(QtCore.QRect(330, 122, 301, 301))
        self.rpm_widget.setStyleSheet(_fromUtf8("border: 0;\n"
"background: transparent;\n"
"border-image: none;"))
        self.rpm_widget.setObjectName(_fromUtf8("rpm_widget"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(640, 0, 3, 582))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.rpm_widget.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.layoutWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.statusBar.raise_()
        self.connectionBar.raise_()
        self.line_5.raise_()
        self.clearAlerts.raise_()
        self.console.raise_()
        self.line_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.batteryDetails, self.closeApplication)
        MainWindow.setTabOrder(self.closeApplication, self.virtKeyboard)
        MainWindow.setTabOrder(self.virtKeyboard, self.connectBMS)
        MainWindow.setTabOrder(self.connectBMS, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.lapTimes)
        MainWindow.setTabOrder(self.lapTimes, self.bestLapTimes)
        MainWindow.setTabOrder(self.bestLapTimes, self.clearLapTimes)
        MainWindow.setTabOrder(self.clearLapTimes, self.startLapTimer)
        MainWindow.setTabOrder(self.startLapTimer, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.statusBar)
        MainWindow.setTabOrder(self.statusBar, self.connectionBar)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.batteryTempBar.setFormat(_translate("MainWindow", "%p *C", None))
        self.voltageBar.setFormat(_translate("MainWindow", "%v V", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Engine </p><p>Temp. </p></body></html>", None))
        self.currentBar.setFormat(_translate("MainWindow", "%v A", None))
        self.engineTempBar.setFormat(_translate("MainWindow", "%p *C", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Battery </p><p>Temp. </p></body></html>", None))
        self.engineSpeedBar.setFormat(_translate("MainWindow", "%v RPM", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Battery<br/>Current </p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Engine<br/>Speed<br/></span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Battery<br/>Voltage </p></body></html>", None))
        item = self.lapTimes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lap Times", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Lap Times", None))
        item = self.bestLapTimes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Best Times", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Best Lap Times", None))
        self.startLapTimer.setText(_translate("MainWindow", "Start Lap Timer", None))
        self.label_9.setText(_translate("MainWindow", "Lap Time:", None))
        self.pushButton.setText(_translate("MainWindow", "Connection", None))
        self.pushButton_3.setText(_translate("MainWindow", "Status", None))
        self.clearAlerts.setText(_translate("MainWindow", "Clear Alerts", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))

