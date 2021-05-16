# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
#main interface

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from cardsUI import cards, cardsAnimated
from progressWinUI import progressWin
from PyQt5 import *

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        print("\nUI -----> STARTING\n")
        # removing default title bar containg close, min-max button
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.roundCorners()
        self.offset = None

        self.initialHomeLayout = QVBoxLayout()
        self.initialHomeStackedWidget = QStackedWidget()
        self.initHomeWidg = QWidget()
        self.cardsWidg = QWidget()
        self.progressWinWidg = QWidget()
        
        self.initHomeUI()
        self.closMinMax(self.initHomeWidg)
        
        self.fromCards = cards.cardsUI(self)
        self.closMinMax(self.cardsWidg)
        self.cardBtnConnection()

        self.fromProgressWin = progressWin.progressWinUI(self)
        self.closMinMax(self.progressWinWidg)
        self.progressWinBtnConnection()

        self.initialHomeStackedWidget.addWidget(self.initHomeWidg)
        self.initialHomeStackedWidget.addWidget(self.cardsWidg)
        self.initialHomeStackedWidget.addWidget(self.progressWinWidg)

        self.initialHomeLayout.addWidget(self.initialHomeStackedWidget)
        self.setCentralWidget(self.initialHomeStackedWidget)

        print("\nUI -----> LIVE\n")

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
    # btnClose, btnMin, btnMax always be active 
    def closMinMax(self, currWidgetInstance):
        print("closeMinMax ----> Called for current widget ==== [WORKING PERFECT]")
        btnClose = QPushButton("X", currWidgetInstance)
        btnClose.setGeometry(15, 15, 13, 13)
        btnClose.setFont(QFont("Alegreya Sans",9))
        btnClose.setStyleSheet("QPushButton {border-radius : 6; background-color: #FF605C;} QPushButton::pressed {background-color: #9c0400}")
        btnClose.clicked.connect(self.onClickClose)
        
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

    # begining UI 
    def initHomeUI(self):
        
        # working icon
        icon1Label = QLabel(self.initHomeWidg)
        icon1Label.setGeometry(QRect(406, 550, 50, 50))
        icon1 = QMovie("icons/write50x50.gif")
        icon1Label.setMovie(icon1)
        icon1.start()

        # working icon
        icon2Label = QLabel(self.initHomeWidg)
        icon2Label.setGeometry(QRect(466, 530, 50, 50))
        icon2 = QMovie("icons/listToTrack50x50.gif")
        icon2Label.setMovie(icon2)
        icon2.start()

        # working icon
        icon3Label = QLabel(self.initHomeWidg)
        icon3Label.setGeometry(QRect(526, 555, 50, 50))
        icon3 = QMovie("icons/completedNotCompleted50x50.gif")
        icon3Label.setMovie(icon3)
        icon3.start()

        brandName = QLabel("Progress Tracker", self.initHomeWidg)
        brandName.setStyleSheet("color: #dadadb;")
        brandName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        brandName.setFont(QFont("Alegreya Sans", 80, 120))
        brandName.setGeometry(QRect(190, 250, 600, 100))

        btnStart = QPushButton("Let's Track", self.initHomeWidg)
        btnStart.setFont(QFont("Alegreya Sans", 24, 60))
        btnStart.setFixedSize(160,60)
        btnStart.setStyleSheet("QPushButton {border-radius : 6; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 white, stop: 0 #facb40, stop:1 #f9a407); color: #0b0d0f} QPushButton::pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #efb506, stop: 1 #b67804);}")
        btnStart.move(410,373)

        btnStartShadow = QGraphicsDropShadowEffect()
        btnStartShadow.setBlurRadius(75)
        btnStartShadow.setColor(QColor(214, 161, 6, 90))
        btnStartShadow.setOffset(0,5)
        btnStart.setGraphicsEffect(btnStartShadow)
        btnStart.clicked.connect(self.letsTrack)

        cpyRgt = QLabel("created by Aman Kumar (Open Source Project)", self.initHomeWidg)
        cpyRgt.setFont(QFont("Alegreya Sans", 15))
        cpyRgt.setStyleSheet("color: #7d7f82;")
        cpyRgt.setAlignment(Qt.AlignCenter)
        cpyRgt.setFixedWidth(600)
        cpyRgt.move(190,662)
    
    # action method
    def cardBtnConnection(self):
        self.fromCards[4].clicked.connect(lambda: self.goBack())
        self.fromCards[0].clicked.connect(lambda: self.initialHomeStackedWidget.setCurrentWidget(self.progressWinWidg))
    
    # action method
    def progressWinBtnConnection(self):
        self.fromProgressWin[1].clicked.connect(lambda: self.goBack())
    
    # issue 2021-0A4 calling one time but printing value increment by one always 
    def goBack(self):
        print("GO BACK: Pressed -----> Going Back ==== [WORKING PERFECT]")
        self.currentIndex = self.initialHomeStackedWidget.currentIndex()
        self.currentIndex -= 1
        self.initialHomeStackedWidget.setCurrentIndex(self.currentIndex)

    # on click letsTrack execute this
    def letsTrack(self):
        print("LetsStart Button: Pressed -----> Start Displaying next UI ==== [WORKING PERFECT]")
        self.initialHomeStackedWidget.setCurrentWidget(self.cardsWidg)
        cardsAnimated.animateCardsBtn(self)

    # action method
    def onClickClose(self):
        print("\nClosed Button: Pressed ----> Closing Window *********")
        self.close()
        print("----------> Windows Closed ==== [WORKING PERFECT]\n")


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
window.setStyleSheet("background-color: #070708;")
window.setFixedSize(980,700)
window.show() # window is hidden by default so we have to show it

progressTrackerApp.exec_()