# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
# CardsUI interface2

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

class cards(QMainWindow):

    def cardsUI(self):

        cardsUIHead = QLabel("Let's Track", self.cardsWidg)
        cardsUIHead.setStyleSheet("color: #dadadb;")
        cardsUIHead.setFont(QFont("Alegreya Sans", 40, 120))
        cardsUIHead.setFixedSize(600,100)
        cardsUIHead.move(150,50)

        self.trackCardBtnBack = QPushButton("<", self.cardsWidg)
        self.trackCardBtnBack.setFont(QFont("Alegreya Sans",40))
        self.trackCardBtnBack.setStyleSheet("QPushButton {color: #ffffff; border-radius : 25; border: 2 solid #ffffff;} QPushButton::pressed {color: #0a0912; border: 2 solid #e9af06; background-color: #e9af06}")
        self.trackCardBtnBack.setFixedSize(50,50)
        self.trackCardBtnBack.move(70,75)
        
        self.trackCardBtn0 = QPushButton("CP Track", self.cardsWidg)
        self.trackCardBtn0.setFont(QFont("Alegreya Sans",30, 100))
        self.trackCardBtn0.setStyleSheet("QPushButton {border-radius : 10; background-color: qlineargradient(x1:, y1:1, x2:1, y2:0, stop:0 white, stop: 0 #facb40, stop:1 #f9a407); color: #0b0d0f} QPushButton::pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #efb506, stop: 1 #b67804);}")
        # self.trackCardBtn0.setFixedSize(260,400)
        self.trackCardBtn0.move(150,180)

        trackCardBtn0Shadow = QGraphicsDropShadowEffect()
        trackCardBtn0Shadow.setBlurRadius(75)
        trackCardBtn0Shadow.setColor(QColor(214, 161, 6, 90))
        trackCardBtn0Shadow.setOffset(0,6)
        self.trackCardBtn0.setGraphicsEffect(trackCardBtn0Shadow)

        self.trackCardBtn1 = QPushButton("+", self.cardsWidg)
        self.trackCardBtn1.setFont(QFont("Alegreya Sans",80))
        self.trackCardBtn1.setStyleSheet("QPushButton {color: #facb40; border-radius : 10; border: 2 solid #facb40; background-color: #0a0912;} QPushButton::pressed {background-color: #9c0400}")
        # self.trackCardBtn1.setFixedSize(180,180)
        self.trackCardBtn1.move(440,180)
        
        self.trackCardBtn2 = QPushButton("+", self.cardsWidg)
        self.trackCardBtn2.setFont(QFont("Alegreya Sans",80))
        self.trackCardBtn2.setStyleSheet("QPushButton {color: #facb40; border-radius : 10; background-color: #4e5257;} QPushButton::pressed {background-color: #9c0400}")
        # self.trackCardBtn2.setFixedSize(180,180)
        self.trackCardBtn2.move(650,180)

        self.trackCardBtn3 = QPushButton("+", self.cardsWidg)
        self.trackCardBtn3.setFont(QFont("Alegreya Sans",180))
        self.trackCardBtn3.setStyleSheet("QPushButton {color: #facb40; border-radius : 10; border: 2 solid #facb40; background-color: #0a0912;} QPushButton::pressed {background-color: #9c0400}")
        # self.trackCardBtn3.setFixedSize(390,190)
        self.trackCardBtn3.move(440,390)

        btnList = [self.trackCardBtn0, self.trackCardBtn1, self.trackCardBtn2, self.trackCardBtn3, self.trackCardBtnBack]

        return btnList

class cardsAnimated(QMainWindow):

    def animateCardsBtn(self):
        self.animateTrackCardBtn0 = QPropertyAnimation(self.trackCardBtn0, b"geometry")
        self.animateTrackCardBtn0.setDuration(200)
        self.animateTrackCardBtn0.setStartValue(QRect(150, 180, 0, 400))
        self.animateTrackCardBtn0.setEndValue(QRect(150, 180, 260, 400))
        self.animateTrackCardBtn0.setEasingCurve(QEasingCurve.InSine)

        self.animateTrackCardBtn1 = QPropertyAnimation(self.trackCardBtn1, b"geometry")
        self.animateTrackCardBtn1.setDuration(200)
        self.animateTrackCardBtn1.setStartValue(QRect(440, 180, 0, 180))
        self.animateTrackCardBtn1.setEndValue(QRect(440, 180, 180, 180))
        self.animateTrackCardBtn1.setEasingCurve(QEasingCurve.InSine)

        self.animateTrackCardBtn2 = QPropertyAnimation(self.trackCardBtn2, b"geometry")
        self.animateTrackCardBtn2.setDuration(200)
        self.animateTrackCardBtn2.setStartValue(QRect(650, 180, 0, 180))
        self.animateTrackCardBtn2.setEndValue(QRect(650, 180, 180, 180))
        self.animateTrackCardBtn2.setEasingCurve(QEasingCurve.InSine)

        self.animateTrackCardBtn3 = QPropertyAnimation(self.trackCardBtn3, b"geometry")
        self.animateTrackCardBtn3.setDuration(200)
        self.animateTrackCardBtn3.setStartValue(QRect(440, 390, 390, -190))
        self.animateTrackCardBtn3.setEndValue(QRect(440, 390, 390, 190))
        # self.animateTrackCardBtn3.setDirection()
        self.animateTrackCardBtn3.setEasingCurve(QEasingCurve.InSine)

        self.groupAnimation = QParallelAnimationGroup()
        self.groupAnimation.addAnimation(self.animateTrackCardBtn0)
        self.groupAnimation.addAnimation(self.animateTrackCardBtn1)
        self.groupAnimation.addAnimation(self.animateTrackCardBtn2)
        self.groupAnimation.addAnimation(self.animateTrackCardBtn3)
        self.groupAnimation.start()
