# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
#main interface

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt5.QFlags import *
from PyQt5 import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.UiComponents()

        # removing default title bar containg close, min-max button
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        # creating rectangle to mask it to give round borders for main-window
        # issue 2021-0A1 [not smooth round bounders, Antialising not work on this]
        self.setFixedSize(980, 700)
        radius = 10
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

        # after removing title bar we cannot move our main window using mouse
        # so here fix
        self.offset = None
        # method for widgets
    def UiComponents(self):
        btnClose = QPushButton("X", self)
        btnClose.setGeometry(15, 15, 13, 13)
        btnClose.setFont(QFont("",9))
        btnClose.setStyleSheet("border-radius : 6; background-color: #FF605C;")
        btnClose.clicked.connect(lambda:self.close())
        
        btnMin = QPushButton("", self)
        btnMin.setGeometry(35, 15, 13, 13)
        btnMin.setFont(QFont("",10))
        btnMin.setStyleSheet("border-radius : 6; background-color: grey;")
        #issue 2021-0A2 btnMin
        # btnMin.clicked.connect(self.hide)
        
        btnMax = QPushButton("", self)
        btnMax.setGeometry(55, 15, 13, 13)
        btnMax.setFont(QFont("",10))
        btnMax.setStyleSheet("border-radius : 6; background-color: grey;")
        #issue 2021-0A3 btnMax
        # btnMax.clicked.connect(self.showFullScreen)
  
    # action method
    def onClickClose(self):
        # self.parent.close()
        print("pressed")
        self.setWindowState(Qt.WindowMinimized)
        # event.accept()

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

# creating custom title bar containg close, min-max button also option title name
# class customBar(QWidget):
#     def __init__(self, parent):
#         super(customBar, self).__init__()

#         self.parent = parent
#         self.layout = QHBoxLayout()
#         self.layout.setContentsMargins(0,0,0,0)
#         # self.title = QLabel("")

#         btnSize = 20

#         self.btnClose = QPushButton("x")
#         self.btnClose.clicked.connect(self.btnCloseClicked)
#         self.btnClose.setFixedSize(btnSize, btnSize)
#         self.btnClose.setStyleSheet("background-color: red;")

        # self.title.setFixedHeight(30)
        # self.title.setAlignment(Qt.AlignCenter)
        # self.title.addWidget(self.title)
    #     self.layout.addWidget(self.btnClose)
    #     self.setLayout(self.layout)
    
    # def btnCloseClicked(self):
    #     self.parent.close()

# comment later
progressTrackerApp = QApplication([])

window = MainWindow()
window.setGeometry(300,60,980,700)
window.setStyleSheet("background-color: #040303;")
window.show()

progressTrackerApp.exec_()
