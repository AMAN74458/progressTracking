# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
# main interface

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

class globalUIView(QMainWindow):

    # creating rectangle to mask it to give round borders for main-window
    # issue 2021-0A1 [not smooth round bounders, Antialising not work on this]
    def roundCorners(self, width, height):
        # self.setFixedSize(980, 700)
        self.setFixedSize(width, height)
        radius = 10
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
    
    # close, minimize, maximize icon fun
    # btnClose, btnMin, btnMax always be active 
    def closMinMax(self, currWidgetInstance, allow):
        print("closeMinMax ----> Called for current widget ==== [WORKING PERFECT]")
        btnClose = QPushButton("X", currWidgetInstance)
        btnClose.setGeometry(15, 15, 13, 13)
        btnClose.setFont(QFont("Alegreya Sans",9))
        btnClose.setStyleSheet("QPushButton {border-radius : 6; background-color: #FF605C;} QPushButton::pressed {background-color: #9c0400}")
        btnClose.clicked.connect(lambda: globalUIView.onClickClose(self, currWidgetInstance, allow))
        
        btnMin = QPushButton("", currWidgetInstance)
        btnMin.setGeometry(35, 15, 13, 13)
        btnMin.setFont(QFont("Alegreya Sans",10))
        btnMin.setStyleSheet("border-radius : 6; background-color: grey;")
        # btnMin.setStyleSheet("QPushButton {border-radius : 6; background-color: #FFBD44;} QPushButton::pressed {background-color: #fca300}")
        #issue 2021-0A2 btnMin
        # btnMin.clicked.connect(self.onClickMin)
        
        btnMax = QPushButton("", currWidgetInstance)
        btnMax.setGeometry(55, 15, 13, 13)
        btnMax.setFont(QFont("",10))
        btnMax.setStyleSheet("border-radius : 6; background-color: grey;")
        #issue 2021-0A3 btnMax
        # btnMax.clicked.connect(self.showFullScreen)
    
        # action method
    def onClickClose(self, currWidgetInstance, allow):
        print("\nClosed Button: Pressed ----> Closing Window ")
        if allow:
            print("\n----------> Closing MainWindow\n")
            self.close()

        else:
            currWidgetInstance.close()
            print("\n----------> Closing DialogWindow\n")

    #issue 2021-0A2 
    # def onClickMin(self):
    #     print("Minimized Pressed")
    #     self.showMinimized()

    # this feature is not available now [maybe later available]
    # def onClickMax(self):
        # print("Maximized Pressed")
        # self.showMaximized()