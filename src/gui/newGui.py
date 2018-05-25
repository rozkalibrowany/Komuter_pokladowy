# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
sys.path.insert(2, os.path.join(sys.path[0], '../..'))
import img.img_rc
from PyQt5 import QtQuickWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setStyleSheet("background-color: rgb(24,24,24);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menuButtonsGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.menuButtonsGroup.setGeometry(QtCore.QRect(0, 0, 81, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButtonsGroup.sizePolicy().hasHeightForWidth())
        self.menuButtonsGroup.setSizePolicy(sizePolicy)
        self.menuButtonsGroup.setMinimumSize(QtCore.QSize(70, 0))
        self.menuButtonsGroup.setMaximumSize(QtCore.QSize(16777215, 480))
        self.menuButtonsGroup.setStyleSheet("/*background-image: url(\":general/general/gradient3.png\"); */\n"
"background-color: rgb(24,24,24);\n"
"")
        self.menuButtonsGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.menuButtonsGroup.setObjectName("menuButtonsGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuButtonsGroup)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hlMain = QtWidgets.QHBoxLayout()
        self.hlMain.setObjectName("hlMain")
        self.vfMain = QtWidgets.QFrame(self.menuButtonsGroup)
        self.vfMain.setMinimumSize(QtCore.QSize(70, 0))
        self.vfMain.setStyleSheet("QPushButton,QFrame {\n"
"border: 1.5px solid #6affcd;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QFrame[chosen=\"true\"] {\n"
"border: none;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"background: #365546;\n"
"}\n"
"QPushButton[chosen=\"true\"]{\n"
"background: #365546; \n"
"}\n"
"\n"
"QLabel[chosen=\"true\"] {\n"
"background: #365546; \n"
"}")
        self.vfMain.setObjectName("vfMain")
        self.vlMain = QtWidgets.QVBoxLayout(self.vfMain)
        self.vlMain.setContentsMargins(0, 0, 0, 0)
        self.vlMain.setObjectName("vlMain")
        self.vlMain_5 = QtWidgets.QVBoxLayout()
        self.vlMain_5.setObjectName("vlMain_5")
        self.hlMainIcon = QtWidgets.QHBoxLayout()
        self.hlMainIcon.setContentsMargins(-1, 0, -1, -1)
        self.hlMainIcon.setObjectName("hlMainIcon")
        self.driveButton = QtWidgets.QPushButton(self.vfMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.driveButton.sizePolicy().hasHeightForWidth())
        self.driveButton.setSizePolicy(sizePolicy)
        self.driveButton.setMinimumSize(QtCore.QSize(0, 65))
        self.driveButton.setStyleSheet("border-image: url(\":44x44/44x44/navigation.png\");")
        self.driveButton.setText("")
        self.driveButton.setObjectName("driveButton")
        self.hlMainIcon.addWidget(self.driveButton)
        self.vlMain_5.addLayout(self.hlMainIcon)
        self.hlMainText = QtWidgets.QHBoxLayout()
        self.hlMainText.setObjectName("hlMainText")
        self.driveLabel = QtWidgets.QLabel(self.vfMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.driveLabel.sizePolicy().hasHeightForWidth())
        self.driveLabel.setSizePolicy(sizePolicy)
        self.driveLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.driveLabel.setStyleSheet("border: 0px; \n"
"font: 11pt \"Purisa\" ;\n"
"color:  #6affcd;")
        self.driveLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.driveLabel.setObjectName("driveLabel")
        self.hlMainText.addWidget(self.driveLabel)
        self.vlMain_5.addLayout(self.hlMainText)
        self.vlMain.addLayout(self.vlMain_5)
        self.hlMain.addWidget(self.vfMain)
        self.verticalLayout.addLayout(self.hlMain)
        self.hlAlerts = QtWidgets.QHBoxLayout()
        self.hlAlerts.setObjectName("hlAlerts")
        self.vfAlerts = QtWidgets.QFrame(self.menuButtonsGroup)
        self.vfAlerts.setMinimumSize(QtCore.QSize(70, 0))
        self.vfAlerts.setStyleSheet("QPushButton,QFrame {\n"
"border: 1.5px solid #6affcd;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QFrame[chosen=\"true\"] {\n"
"border: none;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"background: #365546;\n"
"}\n"
"QPushButton[chosen=\"true\"]{\n"
"background: #365546; \n"
"}\n"
"\n"
"QLabel[chosen=\"true\"] {\n"
"background: #365546; \n"
"}")
        self.vfAlerts.setObjectName("vfAlerts")
        self.vlMain_2 = QtWidgets.QVBoxLayout(self.vfAlerts)
        self.vlMain_2.setContentsMargins(0, 0, 0, 0)
        self.vlMain_2.setObjectName("vlMain_2")
        self.vlAlerts = QtWidgets.QVBoxLayout()
        self.vlAlerts.setObjectName("vlAlerts")
        self.hlAlertsIcon = QtWidgets.QHBoxLayout()
        self.hlAlertsIcon.setContentsMargins(-1, -1, -1, 5)
        self.hlAlertsIcon.setObjectName("hlAlertsIcon")
        self.alertsButton = QtWidgets.QPushButton(self.vfAlerts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alertsButton.sizePolicy().hasHeightForWidth())
        self.alertsButton.setSizePolicy(sizePolicy)
        self.alertsButton.setMinimumSize(QtCore.QSize(0, 65))
        self.alertsButton.setStyleSheet("border-image: url(\":44x44/44x44/message.png\");")
        self.alertsButton.setText("")
        self.alertsButton.setObjectName("alertsButton")
        self.hlAlertsIcon.addWidget(self.alertsButton)
        self.vlAlerts.addLayout(self.hlAlertsIcon)
        self.hlAlertsText = QtWidgets.QHBoxLayout()
        self.hlAlertsText.setObjectName("hlAlertsText")
        self.alertsLabel = QtWidgets.QLabel(self.vfAlerts)
        self.alertsLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.alertsLabel.setStyleSheet("border: 0px; \n"
"font: 11pt \"Purisa\" ;\n"
"color:  #6affcd;")
        self.alertsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.alertsLabel.setObjectName("alertsLabel")
        self.hlAlertsText.addWidget(self.alertsLabel)
        self.vlAlerts.addLayout(self.hlAlertsText)
        self.vlMain_2.addLayout(self.vlAlerts)
        self.hlAlerts.addWidget(self.vfAlerts)
        self.verticalLayout.addLayout(self.hlAlerts)
        self.hlStats = QtWidgets.QHBoxLayout()
        self.hlStats.setObjectName("hlStats")
        self.vfStats = QtWidgets.QFrame(self.menuButtonsGroup)
        self.vfStats.setMinimumSize(QtCore.QSize(70, 0))
        self.vfStats.setStyleSheet("QPushButton,QFrame {\n"
"border: 1.5px solid #6affcd;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QFrame[chosen=\"true\"] {\n"
"border: none;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"background: #365546;\n"
"}\n"
"QPushButton[chosen=\"true\"]{\n"
"background: #365546; \n"
"}\n"
"\n"
"QLabel[chosen=\"true\"] {\n"
"background: #365546; \n"
"}")
        self.vfStats.setObjectName("vfStats")
        self.vlMain_3 = QtWidgets.QVBoxLayout(self.vfStats)
        self.vlMain_3.setContentsMargins(0, 0, 0, 0)
        self.vlMain_3.setObjectName("vlMain_3")
        self.vlStats = QtWidgets.QVBoxLayout()
        self.vlStats.setObjectName("vlStats")
        self.hlStatsIcon = QtWidgets.QHBoxLayout()
        self.hlStatsIcon.setObjectName("hlStatsIcon")
        self.statsButton = QtWidgets.QPushButton(self.vfStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statsButton.sizePolicy().hasHeightForWidth())
        self.statsButton.setSizePolicy(sizePolicy)
        self.statsButton.setMinimumSize(QtCore.QSize(0, 65))
        self.statsButton.setStyleSheet("border-image: url(\":44x44/44x44/statistics.png\");")
        self.statsButton.setText("")
        self.statsButton.setObjectName("statsButton")
        self.hlStatsIcon.addWidget(self.statsButton)
        self.vlStats.addLayout(self.hlStatsIcon)
        self.hlStatsText = QtWidgets.QHBoxLayout()
        self.hlStatsText.setObjectName("hlStatsText")
        self.statsLabel = QtWidgets.QLabel(self.vfStats)
        self.statsLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.statsLabel.setStyleSheet("border: 0px; \n"
"font: 11pt \"Purisa\" ;\n"
"color:  #6affcd;")
        self.statsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsLabel.setObjectName("statsLabel")
        self.hlStatsText.addWidget(self.statsLabel)
        self.vlStats.addLayout(self.hlStatsText)
        self.vlMain_3.addLayout(self.vlStats)
        self.hlStats.addWidget(self.vfStats)
        self.verticalLayout.addLayout(self.hlStats)
        self.hlSettings = QtWidgets.QHBoxLayout()
        self.hlSettings.setObjectName("hlSettings")
        self.vfSettings = QtWidgets.QFrame(self.menuButtonsGroup)
        self.vfSettings.setMinimumSize(QtCore.QSize(70, 0))
        self.vfSettings.setStyleSheet("QPushButton,QFrame {\n"
"border: 1.5px solid #6affcd;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QFrame[chosen=\"true\"] {\n"
"border: none;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"background: #365546;\n"
"}\n"
"QPushButton[chosen=\"true\"]{\n"
"background: #365546; \n"
"}\n"
"\n"
"QLabel[chosen=\"true\"] {\n"
"background: #365546; \n"
"}")
        self.vfSettings.setObjectName("vfSettings")
        self.vlMain_4 = QtWidgets.QVBoxLayout(self.vfSettings)
        self.vlMain_4.setContentsMargins(0, 0, 0, 0)
        self.vlMain_4.setObjectName("vlMain_4")
        self.vlSettings = QtWidgets.QVBoxLayout()
        self.vlSettings.setObjectName("vlSettings")
        self.hlSettingsIcon = QtWidgets.QHBoxLayout()
        self.hlSettingsIcon.setObjectName("hlSettingsIcon")
        self.settingsButton = QtWidgets.QPushButton(self.vfSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        self.settingsButton.setMinimumSize(QtCore.QSize(0, 65))
        self.settingsButton.setStyleSheet("border-image: url(\":44x44/44x44/settings.png\");")
        self.settingsButton.setText("")
        self.settingsButton.setObjectName("settingsButton")
        self.hlSettingsIcon.addWidget(self.settingsButton)
        self.vlSettings.addLayout(self.hlSettingsIcon)
        self.hlSettingsText = QtWidgets.QHBoxLayout()
        self.hlSettingsText.setObjectName("hlSettingsText")
        self.settingsLabel = QtWidgets.QLabel(self.vfSettings)
        self.settingsLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.settingsLabel.setStyleSheet("border: 0px; \n"
"font: 11pt \"Purisa\" ;\n"
"color:  #6affcd;")
        self.settingsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.settingsLabel.setObjectName("settingsLabel")
        self.hlSettingsText.addWidget(self.settingsLabel)
        self.vlSettings.addLayout(self.hlSettingsText)
        self.vlMain_4.addLayout(self.vlSettings)
        self.hlSettings.addWidget(self.vfSettings)
        self.verticalLayout.addLayout(self.hlSettings)
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(88, 0, 711, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setMaximumSize(QtCore.QSize(720, 480))
        self.gridFrame.setStyleSheet("background-color: rgb(24,24,24);\n"
"")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.gridFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.drive = QtWidgets.QWidget()
        self.drive.setStyleSheet("")
        self.drive.setObjectName("drive")
        self.line = QtWidgets.QFrame(self.drive)
        self.line.setGeometry(QtCore.QRect(180, 20, 2, 430))
        self.line.setStyleSheet("background-color: #6affcd")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.drive)
        self.line_2.setGeometry(QtCore.QRect(520, 20, 2, 430))
        self.line_2.setStyleSheet("background-color: #6affcd")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.drive)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 485))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.dvl1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.dvl1.setContentsMargins(0, 0, 0, 0)
        self.dvl1.setObjectName("dvl1")
        self.dhl13 = QtWidgets.QHBoxLayout()
        self.dhl13.setObjectName("dhl13")
        self.throttle = QtQuickWidgets.QQuickWidget(self.verticalLayoutWidget)
        self.throttle.setMinimumSize(QtCore.QSize(0, 155))
        self.throttle.setMaximumSize(QtCore.QSize(167, 16777215))
        self.throttle.setStyleSheet("")
        self.throttle.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.throttle.setObjectName("throttle")
        self.dhl13.addWidget(self.throttle)
        self.dvl1.addLayout(self.dhl13)
        self.dhl12 = QtWidgets.QHBoxLayout()
        self.dhl12.setObjectName("dhl12")
        self.contrTWidget = QtQuickWidgets.QQuickWidget(self.verticalLayoutWidget)
        self.contrTWidget.setMinimumSize(QtCore.QSize(0, 155))
        self.contrTWidget.setMaximumSize(QtCore.QSize(167, 16777215))
        self.contrTWidget.setStyleSheet("")
        self.contrTWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.contrTWidget.setObjectName("contrTWidget")
        self.dhl12.addWidget(self.contrTWidget)
        self.dvl1.addLayout(self.dhl12)
        self.dhl11 = QtWidgets.QHBoxLayout()
        self.dhl11.setObjectName("dhl11")
        self.batteryTWidget = QtQuickWidgets.QQuickWidget(self.verticalLayoutWidget)
        self.batteryTWidget.setMinimumSize(QtCore.QSize(0, 155))
        self.batteryTWidget.setMaximumSize(QtCore.QSize(167, 16777215))
        self.batteryTWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.batteryTWidget.setObjectName("batteryTWidget")
        self.dhl11.addWidget(self.batteryTWidget)
        self.dvl1.addLayout(self.dhl11)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.drive)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 0, 320, 461))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.dvl2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.dvl2.setContentsMargins(0, 0, 0, 0)
        self.dvl2.setObjectName("dvl2")
        self.dhl23 = QtWidgets.QHBoxLayout()
        self.dhl23.setObjectName("dhl23")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.timeLabel.setStyleSheet("font: 26pt \"Halvetica\" ;\n"
"color: #f2f2f2;\n"
"background: transparent;")
        self.timeLabel.setText("")
        self.timeLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.dateLabel.setStyleSheet("font: 75 italic 15pt \"Halvetica\" ;\n"
"color: #a6a6a6;\n"
"background: transparent;")
        self.dateLabel.setText("")
        self.dateLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.dateLabel.setObjectName("dateLabel")
        self.horizontalLayout_4.addWidget(self.dateLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.timerButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.timerButton.setMinimumSize(QtCore.QSize(0, 40))
        self.timerButton.setMaximumSize(QtCore.QSize(16777215, 45))
        self.timerButton.setStyleSheet("QPushButton{\n"
"border: 1.4px solid #00ffc1;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 75 italic 11pt \"Halvetica\" ;\n"
"color: #00ffc1;\n"
"}\n"
"\n"
"QPushButton[clicked=\"true\"] {\n"
"border: 4px solid #00ffc1;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 75 italic 11pt \"Halvetica\" ;\n"
"color: #00ffc1;\n"
"}")
        self.timerButton.setText("")
        self.timerButton.setObjectName("timerButton")
        self.verticalLayout_4.addWidget(self.timerButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 40))
        self.lcdNumber.setMaximumSize(QtCore.QSize(150, 45))
        self.lcdNumber.setSizeIncrement(QtCore.QSize(7, 21))
        self.lcdNumber.setBaseSize(QtCore.QSize(13, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("color: #f2f2f2;\n"
"border: 1.4px solid #00ffc1;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"background: transparent;\n"
"color: #cccccc;")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setLineWidth(4)
        self.lcdNumber.setMidLineWidth(20)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_3.addWidget(self.lcdNumber)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.dhl23.addLayout(self.verticalLayout_2)
        self.dvl2.addLayout(self.dhl23)
        self.dhl22 = QtWidgets.QHBoxLayout()
        self.dhl22.setObjectName("dhl22")
        self.rpm_widget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rpm_widget.sizePolicy().hasHeightForWidth())
        self.rpm_widget.setSizePolicy(sizePolicy)
        self.rpm_widget.setMinimumSize(QtCore.QSize(300, 270))
        self.rpm_widget.setMaximumSize(QtCore.QSize(300, 270))
        self.rpm_widget.setStyleSheet("border: 0;\n"
"background: transparent;\n"
"border-image: none;")
        self.rpm_widget.setObjectName("rpm_widget")
        self.dhl22.addWidget(self.rpm_widget)
        self.dvl2.addLayout(self.dhl22)
        self.horizontalFrame_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.horizontalFrame_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame_4.setObjectName("horizontalFrame_4")
        self.dhl21 = QtWidgets.QHBoxLayout(self.horizontalFrame_4)
        self.dhl21.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.dhl21.setContentsMargins(-1, 0, -1, 9)
        self.dhl21.setObjectName("dhl21")
        self.dvl22 = QtWidgets.QVBoxLayout()
        self.dvl22.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.dvl22.setObjectName("dvl22")
        self.canButton = QtWidgets.QPushButton(self.horizontalFrame_4)
        self.canButton.setMinimumSize(QtCore.QSize(145, 35))
        self.canButton.setStyleSheet("QPushButton {\n"
"border: 1.5px solid #00ffc1;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 75 italic 11pt \"Halvetica\" ;\n"
"color: #00ffc1;\n"
"}\n"
"\n"
"QPushButton[connected=\"true\"] {\n"
"border: 1.5px solid #99ff99;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 75 italic 11pt \"Halvetica\" ;\n"
"color: #99ff99;\n"
"}")
        self.canButton.setText("")
        self.canButton.setObjectName("canButton")
        self.dvl22.addWidget(self.canButton)
        self.dhl21.addLayout(self.dvl22)
        self.dvl21 = QtWidgets.QVBoxLayout()
        self.dvl21.setObjectName("dvl21")
        self.alertStatus = QtWidgets.QLabel(self.horizontalFrame_4)
        self.alertStatus.setMinimumSize(QtCore.QSize(145, 35))
        self.alertStatus.setMaximumSize(QtCore.QSize(145, 16777215))
        self.alertStatus.setStyleSheet("QLabel {\n"
"border: 1.5px solid #99ff99;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 75 italic 11pt \"Halvetica\" ;\n"
"color: #99ff99;\n"
"}\n"
"\n"
"QLabel[isAlert=\"true\"] {\n"
"border: 1.5px solid #ff4d4d;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 75 italic 11pt \"Halvetica\" ;\n"
"color: #ff4d4d;\n"
"}")
        self.alertStatus.setText("")
        self.alertStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.alertStatus.setObjectName("alertStatus")
        self.dvl21.addWidget(self.alertStatus)
        self.dhl21.addLayout(self.dvl21)
        self.dvl2.addWidget(self.horizontalFrame_4)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.drive)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(530, 0, 172, 485))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.dvl3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.dvl3.setContentsMargins(0, 0, 0, 0)
        self.dvl3.setObjectName("dvl3")
        self.dhl33 = QtWidgets.QHBoxLayout()
        self.dhl33.setObjectName("dhl33")
        self.avrPower = QtQuickWidgets.QQuickWidget(self.verticalLayoutWidget_5)
        self.avrPower.setMinimumSize(QtCore.QSize(0, 155))
        self.avrPower.setMaximumSize(QtCore.QSize(167, 16777215))
        self.avrPower.setAutoFillBackground(False)
        self.avrPower.setStyleSheet("")
        self.avrPower.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.avrPower.setObjectName("avrPower")
        self.dhl33.addWidget(self.avrPower)
        self.dvl3.addLayout(self.dhl33)
        self.dhl32 = QtWidgets.QHBoxLayout()
        self.dhl32.setObjectName("dhl32")
        self.batteryCWidget = QtQuickWidgets.QQuickWidget(self.verticalLayoutWidget_5)
        self.batteryCWidget.setMinimumSize(QtCore.QSize(0, 155))
        self.batteryCWidget.setMaximumSize(QtCore.QSize(167, 16777215))
        self.batteryCWidget.setAutoFillBackground(False)
        self.batteryCWidget.setStyleSheet("")
        self.batteryCWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.batteryCWidget.setObjectName("batteryCWidget")
        self.dhl32.addWidget(self.batteryCWidget)
        self.dvl3.addLayout(self.dhl32)
        self.dhl31 = QtWidgets.QHBoxLayout()
        self.dhl31.setObjectName("dhl31")
        self.batteryVWidget = QtQuickWidgets.QQuickWidget(self.verticalLayoutWidget_5)
        self.batteryVWidget.setMinimumSize(QtCore.QSize(0, 155))
        self.batteryVWidget.setMaximumSize(QtCore.QSize(167, 16777215))
        self.batteryVWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.batteryVWidget.setObjectName("batteryVWidget")
        self.dhl31.addWidget(self.batteryVWidget)
        self.dvl3.addLayout(self.dhl31)
        self.line.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.line_2.raise_()
        self.stackedWidget.addWidget(self.drive)
        self.alerts = QtWidgets.QWidget()
        self.alerts.setObjectName("alerts")
        self.frame = QtWidgets.QFrame(self.alerts)
        self.frame.setGeometry(QtCore.QRect(0, 0, 691, 461))
        self.frame.setStyleSheet("QFrame{\n"
"border: 1px solid #00ffc1;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 691, 479))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setStyleSheet("QLabel{\n"
"border: 2px solid #00ffc1;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 75 italic 12pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 435))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 0, 71, 431))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.led_err0 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err0.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err0.setStyleSheet("")
        self.led_err0.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err0.setObjectName("led_err0")
        self.verticalLayout_11.addWidget(self.led_err0)
        self.led_err1 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err1.setLineWidth(0)
        self.led_err1.setObjectName("led_err1")
        self.verticalLayout_11.addWidget(self.led_err1)
        self.led_err2 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err2.setObjectName("led_err2")
        self.verticalLayout_11.addWidget(self.led_err2)
        self.led_err4 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err4.setObjectName("led_err4")
        self.verticalLayout_11.addWidget(self.led_err4)
        self.led_err5 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err5.setObjectName("led_err5")
        self.verticalLayout_11.addWidget(self.led_err5)
        self.led_err6 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err6.setObjectName("led_err6")
        self.verticalLayout_11.addWidget(self.led_err6)
        self.led_err7 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err7.setObjectName("led_err7")
        self.verticalLayout_11.addWidget(self.led_err7)
        self.led_err9 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err9.setObjectName("led_err9")
        self.verticalLayout_11.addWidget(self.led_err9)
        self.led_err10 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err10.setObjectName("led_err10")
        self.verticalLayout_11.addWidget(self.led_err10)
        self.led_err11 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err11.setObjectName("led_err11")
        self.verticalLayout_11.addWidget(self.led_err11)
        self.led_err14 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err14.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err14.setObjectName("led_err14")
        self.verticalLayout_11.addWidget(self.led_err14)
        self.led_err15 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.led_err15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.led_err15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.led_err15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_err15.setObjectName("led_err15")
        self.verticalLayout_11.addWidget(self.led_err15)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(90, 0, 251, 431))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_err0 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err0.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err0.setFont(font)
        self.label_err0.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err0.setObjectName("label_err0")
        self.verticalLayout_12.addWidget(self.label_err0)
        self.label_err1 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err1.setFont(font)
        self.label_err1.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err1.setObjectName("label_err1")
        self.verticalLayout_12.addWidget(self.label_err1)
        self.label_err2 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err2.setFont(font)
        self.label_err2.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err2.setObjectName("label_err2")
        self.verticalLayout_12.addWidget(self.label_err2)
        self.label_err4 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err4.setFont(font)
        self.label_err4.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err4.setObjectName("label_err4")
        self.verticalLayout_12.addWidget(self.label_err4)
        self.label_err5 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err5.setFont(font)
        self.label_err5.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err5.setObjectName("label_err5")
        self.verticalLayout_12.addWidget(self.label_err5)
        self.label_err6 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err6.setFont(font)
        self.label_err6.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err6.setObjectName("label_err6")
        self.verticalLayout_12.addWidget(self.label_err6)
        self.label_err7 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err7.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err7.setFont(font)
        self.label_err7.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err7.setObjectName("label_err7")
        self.verticalLayout_12.addWidget(self.label_err7)
        self.label_err9 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err9.setFont(font)
        self.label_err9.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err9.setObjectName("label_err9")
        self.verticalLayout_12.addWidget(self.label_err9)
        self.label_err10 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err10.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err10.setFont(font)
        self.label_err10.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err10.setObjectName("label_err10")
        self.verticalLayout_12.addWidget(self.label_err10)
        self.label_err11 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err11.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err11.setFont(font)
        self.label_err11.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err11.setObjectName("label_err11")
        self.verticalLayout_12.addWidget(self.label_err11)
        self.label_err14 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err14.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err14.setFont(font)
        self.label_err14.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err14.setObjectName("label_err14")
        self.verticalLayout_12.addWidget(self.label_err14)
        self.label_err15 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_err15.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Halvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_err15.setFont(font)
        self.label_err15.setStyleSheet("QLabel{\n"
"font: 10pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_err15.setObjectName("label_err15")
        self.verticalLayout_12.addWidget(self.label_err15)
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setStyleSheet("QLabel{\n"
"border: 2px solid #00ffc1;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 75 italic 12pt \"Halvetica\" ;\n"
"color: #e6e6e6;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 435))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.alerts)
        self.stats = QtWidgets.QWidget()
        self.stats.setObjectName("stats")
        self.stackedWidget.addWidget(self.stats)
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.stackedWidget.addWidget(self.settings)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.driveLabel.setText(_translate("MainWindow", "Drive"))
        self.alertsLabel.setText(_translate("MainWindow", "Alerts"))
        self.statsLabel.setText(_translate("MainWindow", "Stats"))
        self.settingsLabel.setText(_translate("MainWindow", "Setting"))
        self.label.setText(_translate("MainWindow", "Controller Status"))
        self.label_err0.setText(_translate("MainWindow", "Identification error"))
        self.label_err1.setText(_translate("MainWindow", "Over voltage"))
        self.label_err2.setText(_translate("MainWindow", "Low voltage"))
        self.label_err4.setText(_translate("MainWindow", "motor provide speed feedback"))
        self.label_err5.setText(_translate("MainWindow", "Internal volts fault"))
        self.label_err6.setText(_translate("MainWindow", "Over temperature"))
        self.label_err7.setText(_translate("MainWindow", "Throttle error at power-up"))
        self.label_err9.setText(_translate("MainWindow", "internal reset"))
        self.label_err10.setText(_translate("MainWindow", "hall throttle open"))
        self.label_err11.setText(_translate("MainWindow", "angle sensor open"))
        self.label_err14.setText(_translate("MainWindow", "Motor over temperature"))
        self.label_err15.setText(_translate("MainWindow", "Hall Galvanometer sensor error"))
        self.label_3.setText(_translate("MainWindow", "Battery Status"))
