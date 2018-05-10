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

        pen = QtGui.QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap)

        x1 = self.graphicsView.width()/2
        y1 = self.graphicsView.height()/2

        line_length = self.graphicsView.width()/2 - 10
        angle = (math.radians(ANGLE_RANGE) * value)/MAX_RPM_VALUE
        angle_offset = (360 - ANGLE_RANGE)/2
        x2 = line_length * math.sin(angle + math.radians(angle_offset))
        y2 = -1 * line_length * math.cos(angle + math.radians(angle_offset))

        #print line_length, '|', value, '|', math.degrees(angle), '|', x2, y2
        
        line = QtCore.QLineF(x1, y1 ,x1-x2,y1-y2)
        lineItem = QtWidgets.QGraphicsLineItem(line)
        self.scene.addItem(lineItem)
        lineItem.setPen(pen)


    def updateRPM(self, rpm):
##        if self.activateDial:
##            rpm = self.dial.value()

        number_of_dots = int(rpm/(MAX_RPM_VALUE/len(self.dots)))
        print(number_of_dots)        
        if number_of_dots != self.current_num_of_dots:
            for dot in self.dots[:number_of_dots]:
                if not dot.isVisible():
                    dot.setVisible(True)
            for dot in self.dots[number_of_dots:]:
                if dot.isVisible():
                    dot.setVisible(False)
        self.v_gokart=int(rpm*2.754/216) # Wzor na predkosc gokarta od predkosci obrotowej
        self.rpmNumber.display(self.v_gokart)
        self.current_num_of_dots = number_of_dots

        self.updateLine(rpm)
    
