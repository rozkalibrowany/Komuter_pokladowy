# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'black_window_test2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 634)
        MainWindow.setStyleSheet("")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.VerticalTabs)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-image: url(\"img/tlo.png\");")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 60, 291, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("border-image: url(\"img/transparent.png\");")
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.motorTempBar = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motorTempBar.sizePolicy().hasHeightForWidth())
        self.motorTempBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.motorTempBar.setFont(font)
        self.motorTempBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font: 75 italic 24pt \"Gill Sans MT\" ;\n"
"    color: rgb(24, 112, 194);\n"
"border-image: url(\"img/gradient3.png\");}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #FFFF66;\n"
"    border: 0,6px solid grey;\n"
"    border-radius: 4px;\n"
"    width: 8px;\n"
"    margin:1px;\n"
"\n"
"}\n"
"")
        self.motorTempBar.setMaximum(100)
        self.motorTempBar.setProperty("value", 0)
        self.motorTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.motorTempBar.setObjectName("motorTempBar")
        self.gridLayout_2.addWidget(self.motorTempBar, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-image: url(\"img/gradient3.png\");font: 75 italic 18pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.currentBar = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentBar.sizePolicy().hasHeightForWidth())
        self.currentBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.currentBar.setFont(font)
        self.currentBar.setStyleSheet("QProgressBar {\n"
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
"")
        self.currentBar.setMaximum(400)
        self.currentBar.setProperty("value", 0)
        self.currentBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentBar.setObjectName("currentBar")
        self.gridLayout_2.addWidget(self.currentBar, 1, 1, 1, 1)
        self.controllerTempBar = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controllerTempBar.sizePolicy().hasHeightForWidth())
        self.controllerTempBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.controllerTempBar.setFont(font)
        self.controllerTempBar.setStyleSheet("QProgressBar {\n"
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
"}")
        self.controllerTempBar.setMaximum(100)
        self.controllerTempBar.setProperty("value", 0)
        self.controllerTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.controllerTempBar.setObjectName("controllerTempBar")
        self.gridLayout_2.addWidget(self.controllerTempBar, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image: url(\"img/gradient3.png\");font: 75 italic 18pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.throttleBar = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.throttleBar.sizePolicy().hasHeightForWidth())
        self.throttleBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.throttleBar.setFont(font)
        self.throttleBar.setStyleSheet("QProgressBar {\n"
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
"}")
        self.throttleBar.setMaximum(100)
        self.throttleBar.setProperty("value", 0)
        self.throttleBar.setAlignment(QtCore.Qt.AlignCenter)
        self.throttleBar.setObjectName("throttleBar")
        self.gridLayout_2.addWidget(self.throttleBar, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 18pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.label_2.setLineWidth(3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-image: url(\"img/gradient3.png\");font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 18pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.voltageBar = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voltageBar.sizePolicy().hasHeightForWidth())
        self.voltageBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.voltageBar.setFont(font)
        self.voltageBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"font: 75 italic 24pt \"Gill Sans MT\" ;\n"
"    color: rgb(255, 255, 255);\n"
"border-image: url(\"img/gradient3.png\");}\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #66FF33;\n"
"    border: 0,6px solid grey;\n"
"    border-radius: 4px;\n"
"    width: 8px;\n"
"    margin:1px;\n"
"\n"
"}\n"
"")
        self.voltageBar.setMaximum(120)
        self.voltageBar.setProperty("value", 0)
        self.voltageBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voltageBar.setObjectName("voltageBar")
        self.gridLayout_2.addWidget(self.voltageBar, 0, 1, 1, 1)
        self.motorTempBar.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.controllerTempBar.raise_()
        self.throttleBar.raise_()
        self.label_3.raise_()
        self.currentBar.raise_()
        self.voltageBar.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(640, 1, 381, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("\n"
"border-radius: 10px;\n"
"border-image: url(\"img/transparent.png\");")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.closeApplication = QtWidgets.QPushButton(self.frame_2)
        self.closeApplication.setGeometry(QtCore.QRect(180, 20, 161, 51))
        self.closeApplication.setStyleSheet("QPushButton {border-image: url(\"img/exit_button.png\");\n"
"font: 75 italic 20pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/exit_button_clicked.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}")
        self.closeApplication.setText("")
        self.closeApplication.setAutoRepeatDelay(2500)
        self.closeApplication.setAutoRepeatInterval(2100)
        self.closeApplication.setObjectName("closeApplication")
        self.batteryDetails = QtWidgets.QPushButton(self.frame_2)
        self.batteryDetails.setGeometry(QtCore.QRect(180, 200, 161, 51))
        self.batteryDetails.setStyleSheet("QPushButton {border-image: url(\"img/battery_details_button.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/battery_details_button_clicked.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}")
        self.batteryDetails.setText("")
        self.batteryDetails.setObjectName("batteryDetails")
        self.virtKeyboard = QtWidgets.QPushButton(self.frame_2)
        self.virtKeyboard.setGeometry(QtCore.QRect(180, 140, 161, 51))
        self.virtKeyboard.setStyleSheet("QPushButton {border-image: url(\"img/keyboard_button.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/keyboard_button_clicked.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}")
        self.virtKeyboard.setText("")
        self.virtKeyboard.setObjectName("virtKeyboard")
        self.connectBMS = QtWidgets.QPushButton(self.frame_2)
        self.connectBMS.setGeometry(QtCore.QRect(180, 80, 161, 51))
        self.connectBMS.setStyleSheet("QPushButton {border-image: url(\"img/bms_connect_button.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/bms_connect_button_clicked.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}")
        self.connectBMS.setText("")
        self.connectBMS.setObjectName("connectBMS")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(0, 150, 341, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 161, 271))
        self.tabWidget.setStyleSheet("QTabWidget { /* The tab widget frame */\n"
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
"}")
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lapTimes = QtWidgets.QTableWidget(self.tab)
        self.lapTimes.setGeometry(QtCore.QRect(0, 0, 161, 239))
        self.lapTimes.setMinimumSize(QtCore.QSize(26, 0))
        self.lapTimes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lapTimes.setStyleSheet("QTableWidget {\n"
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
"QTableCornerButton::section {border-image: url(\"img/tlo.png\");}")
        self.lapTimes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lapTimes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lapTimes.setAutoScrollMargin(10)
        self.lapTimes.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.lapTimes.setRowCount(0)
        self.lapTimes.setColumnCount(1)
        self.lapTimes.setObjectName("lapTimes")
        item = QtWidgets.QTableWidgetItem()
        self.lapTimes.setHorizontalHeaderItem(0, item)
        self.lapTimes.horizontalHeader().setCascadingSectionResizes(False)
        self.lapTimes.horizontalHeader().setDefaultSectionSize(138)
        self.lapTimes.horizontalHeader().setMinimumSectionSize(29)
        self.lapTimes.verticalHeader().setDefaultSectionSize(30)
        self.lapTimes.verticalHeader().setSortIndicatorShown(False)
        self.lapTimes.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.bestLapTimes = QtWidgets.QTableWidget(self.tab_2)
        self.bestLapTimes.setGeometry(QtCore.QRect(0, 0, 161, 241))
        self.bestLapTimes.setStyleSheet("QTableWidget {\n"
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
"QTableCornerButton::section {border-image: url(\"img/tlo.png\");}")
        self.bestLapTimes.setObjectName("bestLapTimes")
        self.bestLapTimes.setColumnCount(1)
        self.bestLapTimes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bestLapTimes.setHorizontalHeaderItem(0, item)
        self.bestLapTimes.horizontalHeader().setDefaultSectionSize(144)
        self.bestLapTimes.horizontalHeader().setMinimumSectionSize(29)
        self.tabWidget.addTab(self.tab_2, "")
        self.clearLapTimes = QtWidgets.QPushButton(self.frame_2)
        self.clearLapTimes.setGeometry(QtCore.QRect(180, 260, 161, 51))
        self.clearLapTimes.setStyleSheet("QPushButton {border-image: url(\"img/clear_table.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);\n"
"}\n"
"QPushButton:pressed {border-image: url(\"img/clear_table_clicked.png\");\n"
"font: 75 italic 22pt \"Gill Sans MT\" ;\n"
"color: rgb(36, 36, 36)}")
        self.clearLapTimes.setText("")
        self.clearLapTimes.setObjectName("clearLapTimes")
        self.adekLogo = QtWidgets.QLabel(self.frame_2)
        self.adekLogo.setGeometry(QtCore.QRect(50, 450, 263, 70))
        self.adekLogo.setStyleSheet("border-image: url(\"img/adek3.png\");")
        self.adekLogo.setText("")
        self.adekLogo.setObjectName("adekLogo")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 0, 301, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startLapTimer = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startLapTimer.sizePolicy().hasHeightForWidth())
        self.startLapTimer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.startLapTimer.setFont(font)
        self.startLapTimer.setStyleSheet("QPushButton {border-image: url(\"img/start_lap_button.png\");\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);}\n"
"\n"
"QPushButton:pressed {border-image: url(\"img/start_lap_button_clicked.png\");\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216)\n"
"}")
        self.startLapTimer.setObjectName("startLapTimer")
        self.verticalLayout_2.addWidget(self.startLapTimer)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setSizeIncrement(QtCore.QSize(7, 21))
        self.lcdNumber.setBaseSize(QtCore.QSize(13, 0))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setLineWidth(4)
        self.lcdNumber.setMidLineWidth(10)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 141, 23))
        self.pushButton.setStyleSheet("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 0, 141, 23))
        self.pushButton_3.setStyleSheet("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.statusBar = QtWidgets.QPushButton(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(180, 0, 141, 23))
        self.statusBar.setStyleSheet("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.statusBar.setText("")
        self.statusBar.setObjectName("statusBar")
        self.connectionBar = QtWidgets.QPushButton(self.centralwidget)
        self.connectionBar.setGeometry(QtCore.QRect(180, 30, 141, 23))
        self.connectionBar.setStyleSheet("border-image: url(\"img/gradient3.png\");\n"
"font: 75 italic 16pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);")
        self.connectionBar.setText("")
        self.connectionBar.setObjectName("connectionBar")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(320, 0, 3, 582))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.clearAlerts = QtWidgets.QPushButton(self.centralwidget)
        self.clearAlerts.setGeometry(QtCore.QRect(330, 550, 301, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearAlerts.sizePolicy().hasHeightForWidth())
        self.clearAlerts.setSizePolicy(sizePolicy)
        self.clearAlerts.setMinimumSize(QtCore.QSize(256, 20))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.clearAlerts.setFont(font)
        self.clearAlerts.setStyleSheet("QPushButton {border-image: url(\"img/start_lap_button.png\");\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);}\n"
"\n"
"QPushButton:pressed {border-image: url(\"img/start_lap_button_clicked.png\");\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216)\n"
"}")
        self.clearAlerts.setObjectName("clearAlerts")
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(330, 420, 301, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMinimumSize(QtCore.QSize(0, 0))
        self.console.setMaximumSize(QtCore.QSize(16777215, 380))
        self.console.setStyleSheet("font: 75 italic 11pt;\n"
"border: 5px solid grey;\n"
"border-radius: 10px;\n"
"color: rgb(216, 216, 216);")
        self.console.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.console.setTabStopWidth(73)
        self.console.setObjectName("console")
        self.rpm_widget = QtWidgets.QWidget(self.centralwidget)
        self.rpm_widget.setGeometry(QtCore.QRect(330, 122, 301, 301))
        self.rpm_widget.setStyleSheet("border: 0;\n"
"background: transparent;\n"
"border-image: none;")
        self.rpm_widget.setObjectName("rpm_widget")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(640, 0, 3, 582))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
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
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.motorTempBar.setFormat(_translate("MainWindow", "%p *C"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Controller</p><p>Temp</p></body></html>"))
        self.currentBar.setFormat(_translate("MainWindow", "%v A"))
        self.controllerTempBar.setFormat(_translate("MainWindow", "%p *C"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p> Motor </p><p>Temp</p></body></html>"))
        self.throttleBar.setFormat(_translate("MainWindow", "%v %"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Battery<br/>Current </p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Throttle</span></p><p><span style=\" font-size:18pt;\">signal</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Battery<br/>Voltage </p></body></html>"))
        self.voltageBar.setFormat(_translate("MainWindow", "%v V"))
        item = self.lapTimes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lap Times"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Lap Times"))
        item = self.bestLapTimes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Best Times"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Best Lap Times"))
        self.startLapTimer.setText(_translate("MainWindow", "Start Lap Timer"))
        self.label_9.setText(_translate("MainWindow", "Lap Time:"))
        self.pushButton.setText(_translate("MainWindow", "Connection"))
        self.pushButton_3.setText(_translate("MainWindow", "Status"))
        self.clearAlerts.setText(_translate("MainWindow", "Clear Alerts"))

