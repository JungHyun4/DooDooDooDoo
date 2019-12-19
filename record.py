import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Info():
    def __init__(self):
        super().__init__()

    def info(self, lv, s, la):
        global level, score, lang
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
        nameLabel = QLabel("UserName: ")
        self.nameEdit = QLineEdit()
        self.addButton= QPushButton("Add")
        self.addButton.clicked.connect(self.addButtonClicked)

        layout = QGridLayout()
        layout.addWidget(nameLabel, 0, 0)
        layout.addWidget(self.nameEdit, 0, 1)
        layout.addWidget(self.addButton, 0, 2)
        self.setLayout(layout)

    def addButtonClicked(self):
        self.name = self.nameEdit.text()
        self.close()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.dbfilename = 're'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("Records")
        self.registerButton = QPushButton("Register")
        self.registerButton.clicked.connect(self.registerButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.registerButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def registerButtonClicked(self):
        dlg = LogInDialog()
        dlg.exec_()
        name = dlg.name
        result = {'Name' : name, 'Language' : lang, 'Level' : level, 'Score': score}
        self.scoredb += [result]
        self.showScoreDB()

    def showScoreDB(self):
        keyname = 'Score'
        msg = ''
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in p:
                msg += attr + " : " + str(p[attr]) + "\t"
            msg += "\n"

        self.label.setText(msg)
        self.writeScoreDB()
    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

