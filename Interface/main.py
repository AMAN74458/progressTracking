# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
# main interface

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from globalUI import globalUIView
from cardsUI import cards, cardsAnimated
from progressWinUI import progressWin
from PyQt5 import *

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        print("\nUI -----> STARTING\n")
        
        self.width = 980
        self.height = 700
        # removing default title bar containg close, min-max button
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        globalUIView.roundCorners(self, self.width, self.height)
        self.offset = None

        self.initialHomeLayout = QVBoxLayout()
        self.initialHomeStackedWidget = QStackedWidget()
        self.initHomeWidg = QWidget()
        self.cardsWidg = QWidget()
        self.progressWinWidg = QWidget()
        
        self.initHomeUI()
        globalUIView.closMinMax(self, self.initHomeWidg, True)
        
        cards.cardsUI(self, self.initialHomeStackedWidget)
        globalUIView.closMinMax(self, self.cardsWidg, True)

        progressWin.progressWinUI(self, self.initialHomeStackedWidget)
        globalUIView.closMinMax(self, self.progressWinWidg, True)

        self.initialHomeStackedWidget.addWidget(self.initHomeWidg)
        self.initialHomeStackedWidget.addWidget(self.cardsWidg)
        self.initialHomeStackedWidget.addWidget(self.progressWinWidg)

        self.initialHomeLayout.addWidget(self.initialHomeStackedWidget)
        self.setCentralWidget(self.initialHomeStackedWidget)

        print("\nUI -----> LIVE\n")

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
    def goBack(self, allow):
        print("GO BACK: Pressed -----> Going Back ==== [WORKING PERFECT]")
        self.currentIndex = self.initialHomeStackedWidget.currentIndex()
        self.currentIndex -= 1
        self.initialHomeStackedWidget.setCurrentIndex(self.currentIndex)
        if(allow):
            cardsAnimated.animateCardsBtn(self)

    # on click letsTrack execute this
    def letsTrack(self):
        print("LetsStart Button: Pressed -----> Start Displaying next UI ==== [WORKING PERFECT]")
        self.initialHomeStackedWidget.setCurrentWidget(self.cardsWidg)
        cardsAnimated.animateCardsBtn(self)


#You need one(and only one) QApplication instance per application.
#Pass in sys.argv to allow command line arguments for your app.
#If you know you won't use command line arguments QApplication([]) works too.
progressTrackerApp = QApplication([])

window = MainWindow()
window.setStyleSheet("background-color: #070708;")
window.setFixedSize(980,700)
window.show() # window is hidden by default so we have to show it

progressTrackerApp.exec_()