# developed by Aman Kumar [LPU] => Progress Tracker V-0.01
# CardsUI interface3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from globalUI import globalUIView

class progressWin(QMainWindow):

    def progressWinUI(self, currentWidget):

        progressInfoUIBtnStart = QPushButton("+", self.progressWinWidg)
        progressInfoUIBtnStart.setFont(QFont("Alegreya Sans", 40, 60))
        progressInfoUIBtnStart.setFixedSize(70,70)
        progressInfoUIBtnStart.setStyleSheet("QPushButton {border-radius : 35; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 white, stop: 0 #facb40, stop:1 #f9a407); color: #0b0d0f} QPushButton::pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #efb506, stop: 1 #b67804);}")
        progressInfoUIBtnStart.move(870,600)
        progressInfoUIBtnStart.clicked.connect(progressWin.addTrack)

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
        progressInfoUIBtnBack.clicked.connect(lambda: self.goBack(True))

    def addTrack(self):
        print("\n########################################################\n\nDialog Box -----> Showing [WORKING PROPERLY]\n")
        addTrackDialogs = QDialog()
        addTrackDialogs.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        globalUIView.roundCorners(addTrackDialogs, 490, 350)

        layout = QVBoxLayout(addTrackDialogs)
        addTrackDialogsWidget = QStackedWidget(addTrackDialogs)
        stepOneWidget = QWidget()
        stepTwoWidget = QWidget()
        stepThreeWidget = QWidget()

        addTrackDialogsWidget.addWidget(stepOneWidget)
        addTrackDialogsWidget.addWidget(stepTwoWidget)
        addTrackDialogsWidget.addWidget(stepThreeWidget)
        layout.addWidget(addTrackDialogsWidget)

        buttonStep1 = QPushButton("1", addTrackDialogs)
        buttonStep1.setFont(QFont("Alegreya Sans", 25))
        buttonStep1.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")
        buttonStep1.setGeometry(QRect(110, 50, 50, 50))
        buttonStep1.clicked.connect(lambda: progressWin.step1(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget))

        buttonStep2 = QPushButton("2", addTrackDialogs)
        buttonStep2.setFont(QFont("Alegreya Sans", 25))
        buttonStep2.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")
        buttonStep2.setGeometry(QRect(220, 50, 50, 50))
        buttonStep2.clicked.connect(lambda: progressWin.step2(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget))

        buttonStep3 = QPushButton("3", addTrackDialogs)
        buttonStep3.setFont(QFont("Alegreya Sans",25))
        buttonStep3.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")
        buttonStep3.setGeometry(QRect(330, 50, 50, 50))
        buttonStep3.clicked.connect(lambda: progressWin.step3(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget))


        input0Label = QLabel("What you want to track: ", stepOneWidget)
        input0Label.setStyleSheet("color: #dadadb;")
        input0Label.setFont(QFont("Alegreya Sans", 20))
        input0Label.move(98,120)

        input0 = QLineEdit(stepOneWidget)
        input0.setValidator(QRegExpValidator())
        input0.setMaxLength(50)
        input0.setAlignment(Qt.AlignLeft)
        input0.setFont(QFont("Alegreya Sans",20))
        input0.setFixedSize(250, 50)
        input0.move(98, 160)
        # border is removed in stylesheet it depends on OS which color it will show as a focus 
        input0.setStyleSheet("QLineEdit {color: #dadadb;} QLineEdit:focus {border: 0}")
        progressWin.step1(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget)
        progressWin.nextBtnDialog(self, buttonStep1, buttonStep2, buttonStep3, stepOneWidget, addTrackDialogs, addTrackDialogsWidget, posX1 = 118, posX2 = 235, posY = 240)

        input1Label = QLabel("Enter Date(DDMMYYYY): ", stepTwoWidget)
        input1Label.setStyleSheet("color: #dadadb;")
        input1Label.setFont(QFont("Alegreya Sans", 20))
        input1Label.move(98,120)

        input1 = QLineEdit(stepTwoWidget)
        input1.setValidator(QIntValidator())
        input1.setMaxLength(8)
        input1.setAlignment(Qt.AlignLeft)
        input1.setFont(QFont("Alegreya Sans",20))
        input1.setFixedSize(250, 50)
        input1.move(98, 160)
        # border is removed in stylesheet it depends on OS which color it will show as a focus 
        input1.setStyleSheet("QLineEdit {color: #dadadb;} QLineEdit:focus {border: 0}")
        progressWin.nextBtnDialog(self, buttonStep1, buttonStep2, buttonStep3, stepTwoWidget, addTrackDialogs, addTrackDialogsWidget, posX1 = 118, posX2 = 235, posY = 240)

        input2Label = QLabel("How many times you want to\nrepeat it in a day: ", stepThreeWidget)
        input2Label.setStyleSheet("color: #dadadb;")
        input2Label.setFont(QFont("Alegreya Sans", 20))
        input2Label.move(98,120)

        input2 = QLineEdit(stepThreeWidget)
        input2.setValidator(QIntValidator())
        input2.setMaxLength(4)
        input2.setAlignment(Qt.AlignLeft)
        input2.setFont(QFont("Alegreya Sans", 20))
        input2.setFixedSize(250, 50)
        input2.move(98, 180)
        # border is removed in stylesheet it depends on OS which color it will show as a focus 
        input2.setStyleSheet("QLineEdit {color: #dadadb;} QLineEdit:focus {border: 0}")
        progressWin.nextBtnDialog(self, buttonStep1, buttonStep2, buttonStep3, stepThreeWidget, addTrackDialogs, addTrackDialogsWidget, posX1 = 118, posX2 = 235, posY = 250)

        addTrackDialogs.setStyleSheet("background-color: #202025;")
        addTrackDialogs.exec_()

    def step1(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget):
        print("\nstep1 -----> Showing UI [WORKING PROPERLY]")
        buttonStep1.setStyleSheet("QPushButton {text-align: center; background-color: #facb40; border-radius: 25;}")
        buttonStep2.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")
        buttonStep3.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")

        addTrackDialogsWidget.setCurrentIndex(0)

    def step2(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget):
        print("step2 -----> Showing UI [WORKING PROPERLY]")
        buttonStep2.setStyleSheet("QPushButton {text-align: center; background-color: #facb40; border-radius: 25;}")
        buttonStep1.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")
        buttonStep3.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")

        addTrackDialogsWidget.setCurrentIndex(1)

    def step3(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget):
        print("step3 -----> Showing UI [WORKING PROPERLY]")
        buttonStep3.setStyleSheet("QPushButton {text-align: center; background-color: #facb40; border-radius: 25;}")
        buttonStep1.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")
        buttonStep2.setStyleSheet("QPushButton {text-align: center; color: #facb40; border-radius : 25; border: 2 solid #facb40;}")

        addTrackDialogsWidget.setCurrentIndex(2)

    def nextBtnDialog(self, buttonStep1, buttonStep2, buttonStep3, currentWidget, addTrackDialogs, addTrackDialogsWidget, posX1, posX2, posY):
        print("Showing Cancel and Done buttons -----> [WORKING PERFECTLY]")

        cancelBtn = QPushButton("Cancel", currentWidget)
        cancelBtn.setFont(QFont("Alegreya Sans", 20, 60))
        cancelBtn.setStyleSheet("QPushButton {text-align: center; background-color: #FF605C; border-radius : 6;}")
        cancelBtn.setFixedSize(90, 30)
        cancelBtn.move(posX1, posY)
        cancelBtn.clicked.connect(lambda: progressWin.closeDialog(self, addTrackDialogs))

        nextBtn = QPushButton("Done", currentWidget)
        nextBtn.setFont(QFont("Alegreya Sans", 20, 60))
        nextBtn.setStyleSheet("QPushButton {text-align: center; background-color: #facb40; border-radius : 6;}")
        nextBtn.setFixedSize(90, 30)
        nextBtn.move(posX2, posY)
        nextBtn.clicked.connect(lambda: progressWin.nextPageDialog(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget))
    
    def closeDialog(self, addTrackDialogs):
        print("\nCancel Button Pressed -----> Closed [WORKING PERFECTLY]\n")
        addTrackDialogs.close()

    def nextPageDialog(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget):
        limit = addTrackDialogsWidget.count()
        currentIdx = addTrackDialogsWidget.currentIndex()
        currentIdx += 1 
        if limit - 1 >= currentIdx:
            print("\nNext Button Pressed -----> Showing Next Diaglog UI [WORKING PROPERLY]")
            # addTrackDialogsWidget.setCurrentIndex(currentIdx)
            if currentIdx == 1:
                progressWin.step2(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget)
            if currentIdx == 2:
                progressWin.step3(self, buttonStep1, buttonStep2, buttonStep3, addTrackDialogsWidget)




