# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
#main interface

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from cardsUI import cards
from PyQt5 import *


import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # removing default title bar containg close, min-max button
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.roundCorners()
        self.offset = None

        self.initialHomeLayout = QStackedLayout()
        self.subVerLayout = QVBoxLayout()
        self.initialHomeWidgets = QWidget()
        self.initialHomeWidgets.setLayout(self.initialHomeLayout)
        self.setCentralWidget(self.initialHomeWidgets)
        self.initHomeUI()
        self.closMinMax()


    # creating rectangle to mask it to give round borders for main-window
    # issue 2021-0A1 [not smooth round bounders, Antialising not work on this]
    def roundCorners(self):
        self.setFixedSize(980, 700)
        radius = 10
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
    
    # close, minimize, maximize icon fun
    def closMinMax(self):
        print("I am Called")
        # btnClose, btnMin, btnMax always be active 
        btnClose = QPushButton("X", self)
        btnClose.setGeometry(15, 15, 13, 13)
        btnClose.setFont(QFont("Alegreya Sans",9))
        btnClose.setStyleSheet("QPushButton {border-radius : 6; background-color: #FF605C;} QPushButton::pressed {background-color: #9c0400}")
        btnClose.clicked.connect(self.onClickClose)
        
        btnMin = QPushButton("", self)
        btnMin.setGeometry(35, 15, 13, 13)
        btnMin.setFont(QFont("Alegreya Sans",10))
        btnMin.setStyleSheet("border-radius : 6; background-color: grey;")
        # btnMin.setStyleSheet("QPushButton {border-radius : 6; background-color: #FFBD44;} QPushButton::pressed {background-color: #fca300}")
        #issue 2021-0A2 btnMin
        # btnMin.clicked.connect(self.onClickMin)
        
        btnMax = QPushButton("", self)
        btnMax.setGeometry(55, 15, 13, 13)
        btnMax.setFont(QFont("",10))
        btnMax.setStyleSheet("border-radius : 6; background-color: grey;")

    # begining UI 
    def initHomeUI(self):

        brandName = QLabel("Progress Tracker")
        brandName.setStyleSheet("color: #dadadb;")
        brandName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        brandName.setFont(QFont("Alegreya Sans", 80, 120))
        brandName.setFixedSize(600,100)
        brandName.move(190,250)
        self.subVerLayout.addWidget(brandName)

        btnStart = QPushButton("Let's Track", self)
        btnStart.setFont(QFont("Alegreya Sans", 24, 60))
        btnStart.setFixedSize(160,60)
        btnStart.setStyleSheet("QPushButton {border-radius : 30; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 white, stop: 0 #facb40, stop:1 #f9a407); color: #0b0d0f} QPushButton::pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #efb506, stop: 1 #b67804);}")
        btnStart.move(410,373)
        self.subVerLayout.addWidget(btnStart)

        btnStartShadow = QGraphicsDropShadowEffect()
        btnStartShadow.setBlurRadius(75)
        btnStartShadow.setColor(QColor(214, 161, 6, 90))
        btnStartShadow.setOffset(0,5)
        btnStart.setGraphicsEffect(btnStartShadow)
        btnStart.clicked.connect(self.letsTrack)

        self.initialHomeLayout.addChildLayout(self.subVerLayout)

        cpyRgt = QLabel("created by Aman Kumar (Open Source Project)", self)
        cpyRgt.setFont(QFont("Alegreya Sans", 15))
        cpyRgt.setStyleSheet("color: #7d7f82;")
        cpyRgt.setAlignment(Qt.AlignCenter)
        cpyRgt.setFixedWidth(600)
        cpyRgt.move(190,662)


    def delLayout(self):
        while self.subVerLayout.count():
            item = self.subVerLayout.itemAt(0)
            if item != None :
                widget = item.widget()
                if widget != None:
                    self.subVerLayout.removeWidget(widget)
                    widget.deleteLater()  
            print("Delteing Layer: Completed")  

    # on click letsTrack execute this
    def letsTrack(self):
        print("letsStart Button: Pressed")
        self.delLayout()
        Currlay = cards.cardsUI(self)
        self.initialHomeLayout.addChildLayout(Currlay)

    # action method
    def onClickClose(self):
        print("Closed Button: Pressed")
        self.close()

    
    #issue 2021-0A2 
    # def onClickMin(self):
    #     print("Minimized Pressed")
    #     self.showMinimized()

    # this feature is not available now [maybe later available]
    # def onClickMax(self):
        # print("Maximized Pressed")
        # self.showMaximized()


#You need one(and only one) QApplication instance per application.
#Pass in sys.argv to allow command line arguments for your app.
#If you know you won't use command line arguments QApplication([]) works too.
progressTrackerApp = QApplication([])

window = MainWindow()
window.setStyleSheet("background-color: #0a0912;")
window.setFixedSize(980,700)
window.show() # window is hidden by default so we have to show it

progressTrackerApp.exec_()