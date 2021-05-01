# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
# CardsUI interface2

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

class cards(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

    def cardsUI(self):
        layout = QVBoxLayout()

        cardsUIHead = QLabel("Let's Track")
        cardsUIHead.setStyleSheet("color: #dadadb;")
        # cardsUIHead.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        cardsUIHead.setFont(QFont("Alegreya Sans", 40, 120))
        cardsUIHead.setFixedSize(600,100)
        cardsUIHead.move(150,50)
        layout.addWidget(cardsUIHead)

        trackCardBtnBack = QPushButton("<", self)
        trackCardBtnBack.setFont(QFont("Alegreya Sans",40))
        trackCardBtnBack.setStyleSheet("QPushButton {color: #ffffff; border-radius : 25; border: 2 solid #ffffff;} QPushButton::pressed {color: #0a0912; border: 2 solid #e9af06; background-color: #e9af06}")
        trackCardBtnBack.setFixedSize(50,50)
        trackCardBtnBack.move(70,75)
        # issue 2021-0A4 [function is not exxecuting inside uiCardsBackBtnClick]
        trackCardBtnBack.clicked.connect(cards.uiCardsBackBtnClick)
        layout.addWidget(trackCardBtnBack)
        
        trackCardBtn0 = QPushButton("CP Track", self)
        trackCardBtn0.setFont(QFont("Alegreya Sans",30, 100))
        trackCardBtn0.setStyleSheet("QPushButton {border-radius : 10; background-color: #facb40;} QPushButton::pressed {background-color: #e9af06}")
        trackCardBtn0.setFixedSize(260,400)
        trackCardBtn0.move(150,180)
        layout.addWidget(trackCardBtn0)

        trackCardBtn0Shadow = QGraphicsDropShadowEffect()
        trackCardBtn0Shadow.setBlurRadius(75)
        trackCardBtn0Shadow.setColor(QColor(214, 161, 6, 90))
        trackCardBtn0Shadow.setOffset(0,6)
        trackCardBtn0.setGraphicsEffect(trackCardBtn0Shadow)

        trackCardBtn1 = QPushButton("+", self)
        trackCardBtn1.setFont(QFont("Alegreya Sans",80))
        trackCardBtn1.setStyleSheet("QPushButton {color: #facb40; border-radius : 10; border: 2 solid #facb40; background-color: #0a0912;} QPushButton::pressed {background-color: #9c0400}")
        trackCardBtn1.setFixedSize(180,180)
        trackCardBtn1.move(440,180)
        layout.addWidget(trackCardBtn1)
        
        trackCardBtn2 = QPushButton("+", self)
        trackCardBtn2.setFont(QFont("Alegreya Sans",80))
        trackCardBtn2.setStyleSheet("QPushButton {color: #facb40; border-radius : 10; background-color: #4e5257;} QPushButton::pressed {background-color: #9c0400}")
        trackCardBtn2.setFixedSize(180,180)
        trackCardBtn2.move(650,180)
        layout.addWidget(trackCardBtn2)

        trackCardBtn3 = QPushButton("+", self)
        trackCardBtn3.setFont(QFont("Alegreya Sans",180))
        trackCardBtn3.setStyleSheet("QPushButton {color: #facb40; border-radius : 10; border: 2 solid #facb40; background-color: #0a0912;} QPushButton::pressed {background-color: #9c0400}")
        trackCardBtn3.setFixedSize(390,190)
        trackCardBtn3.move(440,390)
        layout.addWidget(trackCardBtn3)

        return layout
    
    # issue 2021-0A4
    def uiCardsBackBtnClick(self):
        print("Back Button: Pressed")
        # MainWindow().initHomeUI()