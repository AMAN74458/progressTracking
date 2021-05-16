# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
# CardsUI interface2

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

class progressWin(QMainWindow):

    def progressWinUI(self):

        progressInfoUIBtnStart = QPushButton("+", self.progressWinWidg)
        progressInfoUIBtnStart.setFont(QFont("Alegreya Sans", 40, 60))
        progressInfoUIBtnStart.setFixedSize(70,70)
        progressInfoUIBtnStart.setStyleSheet("QPushButton {border-radius : 35; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 white, stop: 0 #facb40, stop:1 #f9a407); color: #0b0d0f} QPushButton::pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #efb506, stop: 1 #b67804);}")
        progressInfoUIBtnStart.move(870,600)

        progressInfoUIHead = QLabel("Tracking", self.progressWinWidg)
        progressInfoUIHead.setStyleSheet("color: #dadadb;")
        progressInfoUIHead.setFont(QFont("Alegreya Sans", 40, 120))
        progressInfoUIHead.setFixedSize(600,100)
        progressInfoUIHead.move(150,50)

        progressInfoUIBtnBack = QPushButton("<", self.progressWinWidg)
        progressInfoUIBtnBack.setFont(QFont("Alegreya Sans",40))
        progressInfoUIBtnBack.setStyleSheet("QPushButton {color: #ffffff; border-radius : 25; border: 2 solid #ffffff;} QPushButton::pressed {color: #0a0912; border: 2 solid #e9af06; background-color: #e9af06}")
        progressInfoUIBtnBack.setFixedSize(50,50)
        progressInfoUIBtnBack.move(70,75)

        btnList = [progressInfoUIBtnStart, progressInfoUIBtnBack]

        return btnList
