# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
#main interface

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # removing default title bar containg close, min-max button
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.roundCorners()
        # brTitle() should always be above closeMinButtons()
        self.brTitle()
        self.closeMinMaxButtons()
        self.cpyRight()

        # after removing title bar we cannot move our main window using mouse
        # so here fix..
        self.offset = None

    #...fix continue
    # when mouse button is pressed or tap
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    #when we move our mouse
    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    #when we release mouse button
    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
    #...fix end
    
    # creating rectangle to mask it to give round borders for main-window
    # issue 2021-0A1 [not smooth round bounders, Antialising not work on this]
    def roundCorners(self):
        self.setFixedSize(980, 700)
        radius = 10
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

    #custom close, minimize and maximized button UI function
    def closeMinMaxButtons(self):
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
        btnMin.clicked.connect(self.onClickMin)
        
        btnMax = QPushButton("", self)
        btnMax.setGeometry(55, 15, 13, 13)
        btnMax.setFont(QFont("",10))
        btnMax.setStyleSheet("border-radius : 6; background-color: grey;")
        #issue 2021-0A3 btnMax
        # btnMax.clicked.connect(self.onClickMax)
    
    # action method
    def onClickClose(self):
        print("Closed Pressed")
        self.close()
    
    #issue 2021-0A2 
    def onClickMin(self):
        print("Minimized Pressed")
        self.showMinimized()

    # this feature is not available now [maybe later available]
    # def onClickMax(self):
        # print("Maximized Pressed")
        # self.showMaximized()
    
    def brTitle(self):
        layoutBN = QVBoxLayout()
        brandName = QLabel("Progress Tracker")
        brandName.setFont(QFont("Alegreya Sans", 80, 120))
        # print(brandName.size())
        # brandName.setStyleSheet("color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(30, 50, 20, 255));")
        brandName.setStyleSheet("color: #dadadb;")
        # brandName.setStyleSheet("background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #00ffff, stop: 1 #ff000f);")
        brandName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layoutBN.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        brandName.setFixedSize(600,100)
        layoutBN.addWidget(brandName)

        layoutBN.setSpacing(23)
        btnStart = QPushButton("Let's Track", self)
        btnStart.setFont(QFont("Alegreya Sans", 24, 60))
        btnStart.setFixedSize(160,60)
        layoutBN.addWidget(btnStart, 0, alignment=Qt.AlignCenter)
        btnStart.setStyleSheet("QPushButton {border-radius : 30; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 white, stop: 0 #facb40, stop:1 #f9a407); color: #0b0d0f} QPushButton::pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #efb506, stop: 1 #b67804);}")
        btnStart.clicked.connect(self.letsTrack)

        # cpyRgt = QLabel("created by Aman Kumar (Open Source Project)", self)
        # cpyRgt.setFont(QFont("Alegreya Sans", 20))
        # cpyRgt.setStyleSheet("color: red;")
        # cpyRgt.setStyleSheet("background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #00ffff, stop: 1 #ff000f);")
        # layoutBN.addWidget(cpyRgt)
        # cpyRgt.setAlignment(Qt.AlignCenter)
        # print(cpyRgt.size())
        
        widget = QWidget()
        widget.setLayout(layoutBN)
        self.setCentralWidget(widget)
        
    # on click letsTrack execute this
    def letsTrack(self):
        print("letsStart Working")

    # developer info
    def cpyRight(self):
        cpyRgt = QLabel("created by Aman Kumar (Open Source Project)", self)
        cpyRgt.setFont(QFont("Alegreya Sans", 15))
        cpyRgt.setStyleSheet("color: #7d7f82;")
        # cpyRgt.setStyleSheet("background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #00ffff, stop: 1 #ff000f);")
        cpyRgt.setFixedWidth(600)
        cpyRgt.setAlignment(Qt.AlignCenter)
        cpyRgt.move(190,662)
        self.show()



#You need one(and only one) QApplication instance per application.
#Pass in sys.argv to allow command line arguments for your app.
#If you know you won't use command line arguments QApplication([]) works too.
progressTrackerApp = QApplication([])

window = MainWindow()
window.setGeometry(300,60,980,700)
window.setStyleSheet("background-color: #0a0912;")
window.show() # window is hidden by default so we have to show it

progressTrackerApp.exec_()
