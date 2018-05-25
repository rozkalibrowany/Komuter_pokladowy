from PyQt5 import QtCore, QtGui, QtWidgets
from .rpm_widget import Ui_rpm_widget
import math
from src.modules.settings import *

class RPM_Widget(QtWidgets.QWidget, Ui_rpm_widget):
    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet('QWidget {background: transparent;}')
        self.init_rpm_widget()

    def init_rpm_widget(self):
        self.dots = self.dots_widget.findChildren(QtWidgets.QLabel)

        for dot in self.dots:
            dot.setVisible(False)

        self.current_num_of_dots = 0
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setSceneRect(0,0,self.graphicsView.frameSize().width(),self.graphicsView.frameSize().height())
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.updateLine(0)

    def updateLine(self, value):

        self.scene.clear()

        colorName = '#6affcd'
        dotColorName = '#22e2a2'
        color = QtGui.QColor(0,0,0)
        color.setNamedColor(colorName)
        themeBrush = QtGui.QBrush(color)
        pen = QtGui.QPen(themeBrush, 4, QtCore.Qt.SolidLine, QtCore.Qt.FlatCap)
        pintopPen = QtGui.QPen(themeBrush, 11, QtCore.Qt.SolidLine, QtCore.Qt.FlatCap)

        x1 = self.graphicsView.width()/2
        y1 = self.graphicsView.height()/2

        line_length = self.graphicsView.width()/2 - 10
        angle = (math.radians(ANGLE_RANGE) * value)/MAX_RPM_VALUE
        angle_offset = (360 - ANGLE_RANGE)/2
        x2 = line_length * math.sin(angle + math.radians(angle_offset))
        y2 = -1 * line_length * math.cos(angle + math.radians(angle_offset))

        # draw pintop
        pintop = QtCore.QRectF(x1-2, y1-3 ,10, 10)
        pintopItem = QtWidgets.QGraphicsEllipseItem(pintop)
        self.scene.addItem(pintopItem)
        pintopItem.setPen(pintopPen)

        # draw line
        line = QtCore.QLineF(x1, y1 ,x1-x2,y1-y2)
        lineItem = QtWidgets.QGraphicsLineItem(line)
        self.scene.addItem(lineItem)
        lineItem.setPen(pen)
        # draw dot
        color.setNamedColor(dotColorName)
        themeBrush = QtGui.QBrush(color)
        dotPen = QtGui.QPen(themeBrush, 6, QtCore.Qt.SolidLine, QtCore.Qt.FlatCap)
        dot = QtCore.QRectF(x1, y1 ,5, 4)
        dotItem = QtWidgets.QGraphicsEllipseItem(dot)
        self.scene.addItem(dotItem)
        pintopItem.setPen(pintopPen)

        # draw line
        line = QtCore.QLineF(x1, y1 ,x1-x2,y1-y2)
        lineItem = QtWidgets.QGraphicsLineItem(line)
        self.scene.addItem(lineItem)
        lineItem.setPen(pen)
        pintop = QtCore.QRectF(x1, y1 ,4, 4)

        # draw dot
        color.setNamedColor(dotColorName)
        themeBrush = QtGui.QBrush(color)
        dotPen = QtGui.QPen(themeBrush, 6, QtCore.Qt.SolidLine, QtCore.Qt.FlatCap)
        dot = QtCore.QRectF(x1, y1 ,5, 4)
        dotItem = QtWidgets.QGraphicsEllipseItem(dot)
        self.scene.addItem(dotItem)
        dotItem.setPen(dotPen)


    def updateRPM(self, rpm):
##        if self.activateDial:
##            rpm = self.dial.value()
        self.rpmNumber.display(int(rpm/100))
        number_of_dots = int(rpm/(MAX_RPM_VALUE/len(self.dots)))
        print(number_of_dots)
        if number_of_dots != self.current_num_of_dots:
            for dot in self.dots[:number_of_dots]:
                if not dot.isVisible():
                    dot.setVisible(True)
            for dot in self.dots[number_of_dots:]:
                if dot.isVisible():
                    dot.setVisible(False)
        v_gokart=int(rpm*0.02827) # Wzor na predkosc gokarta od predkosci obrotowej
        self.rpmNumber.display(v_gokart)
        self.current_num_of_dots = number_of_dots
        self.updateLine(rpm)

