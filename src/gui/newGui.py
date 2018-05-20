# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
sys.path.insert(2, os.path.join(sys.path[0], '../..'))
import img.img_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setStyleSheet("background-image: url(\":general/general/gradient3.png\");\n"
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
"background-color: black;")
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
        self.gridFrame.setStyleSheet("background-image: url(\":general/general/gradient3.png\");\n"
"")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.gridFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.drive = QtWidgets.QWidget()
        self.drive.setObjectName("drive")
        self.line = QtWidgets.QFrame(self.drive)
        self.line.setGeometry(QtCore.QRect(130, 20, 2, 430))
        self.line.setStyleSheet("background-color: #6affcd")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.drive)
        self.line_2.setGeometry(QtCore.QRect(450, 20, 2, 430))
        self.line_2.setStyleSheet("background-color: #6affcd")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.rpm_widget = QtWidgets.QWidget(self.drive)
        self.rpm_widget.setGeometry(QtCore.QRect(140, 100, 301, 301))
        self.rpm_widget.setStyleSheet("border: 0;\n"
"background: transparent;\n"
"border-image: none;")
        self.rpm_widget.setObjectName("rpm_widget")
        self.stackedWidget.addWidget(self.drive)
        self.alerts = QtWidgets.QWidget()
        self.alerts.setObjectName("alerts")
        self.stackedWidget.addWidget(self.alerts)
        self.stats = QtWidgets.QWidget()
        self.stats.setObjectName("stats")
        self.stackedWidget.addWidget(self.stats)
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.stackedWidget.addWidget(self.settings)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.driveLabel.setText(_translate("MainWindow", "Drive"))
        self.alertsLabel.setText(_translate("MainWindow", "Alerts"))
        self.statsLabel.setText(_translate("MainWindow", "Stats"))
        self.settingsLabel.setText(_translate("MainWindow", "Setting"))

