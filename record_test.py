import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ass():
    def __init__(self):
        super().__init__()

    def hi(self,lv,s,la):
        global level,score,lang
        level = lv
        score = s
        lang = la

class LogInDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.name = None

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("Sign In")

        label1 = QLabel("UserName: ")

        self.lineEdit1 = QLineEdit()
        self.pushButton1= QPushButton("Add")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.name = self.lineEdit1.text()
        self.close()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.dbfilename = 'hihihi'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("Records")
        self.pushButton = QPushButton("Register")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        dlg = LogInDialog()
        dlg.exec_()
        name = dlg.name
        result = {'Name' : 'leejung', 'Language' : 'korr', 'Level' : 'expert', 'Score': 77}
        self.scoredb += [result]
        self.showScoreDB()

    def showScoreDB(self):
        keyname = 'Score'
        msg = ''
        result = {'Name': 'leejung', 'Language': 'korr', 'Level': 'expert', 'Score': 77}
        self.scoredb4=[]
        self.scoredb4 += [result]
        for p in sorted(self.scoredb4, key=lambda person: person[keyname]):
            for attr in p:
                msg += attr + " : " + str(p[attr]) + " , "
            msg += "\n"
        self.label.setText(msg)
        self.writeScoreDB()
    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb4 = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb4, fH)
        fH.close()

