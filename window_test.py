from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
import time
import random
import record_test

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        global xyList, wordList
        xyList = []
        wordList = []

        # GRID
        grid = QGridLayout()
        self.labels = [[x for x in range(2)], [x for x in range(2)], [x for x in range(2)]]

        for i in range(2):
            for j in range(2):
                self.labels[i][j] = QLabel('')
                grid.addWidget(self.labels[i][j], i, j)


        # 컨트롤 레이아웃 박스
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        # 한글 영어 선택
        self.lang = QComboBox()
        self.lang.addItem('Kor')
        self.lang.addItem('Eng')
        self.lang.setCurrentIndex(0)
        self.hbox2.addWidget(self.lang)

        # 난이도
        self.level = QComboBox()
        self.level.addItem('Beginner')
        self.level.addItem('Intermediate')
        self.level.addItem('Expert')
        self.level.setCurrentIndex(0)
        self.hbox2.addWidget(self.level)

        # 단어 입력창
        self.edit = QLineEdit()
        self.edit.setEnabled(False)
        self.hbox2.addWidget(self.edit)

        # 점수 입력칸
        self.ScoreLabel = QLabel('Score:')
        self.s = 0
        self.score = QLineEdit(str(self.s))
        self.score.setReadOnly(True)
        self.hbox4.addWidget(self.ScoreLabel)
        self.hbox4.addWidget(self.score)

        # 목숨 칸
        self.LifeLabel = QLabel('Life:')
        self.life =' 😯 😯 😯 😯 😯 '
        self.lifeEdit = QLineEdit(self.life)
        self.lifeEdit.setReadOnly(True)
        self.hbox4.addWidget(self.LifeLabel)
        self.hbox4.addWidget(self.lifeEdit)

        # 게임 시작버튼
        self.btn = QPushButton('Start')
        self.btn.setCheckable(True)
        self.btn.toggled.connect(self.toggleButton)
        self.hbox2.addWidget(self.btn)

        self.vbox1.addLayout(self.hbox4)
        self.vbox1.addLayout(self.hbox2)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(grid)
        self.vbox.addLayout(self.vbox1)
        self.setLayout(self.vbox)
        self.setGeometry(300,300,700,700)
        self.setWindowTitle('MoleTyping')
        self.show()
    def setText(self, x, y, z):

            words = ["hi", "car", "topic", "apple"]


            if self.labels[x][y].text() == '':
                self.labels[x][y].setText(words[z])
                wordList.append(words[z])
                xyList.append([x,y])


    def test(self,speed):
        if self.flag :
            self.speed=speed
            a = 0
            if a == 0 :
                if self.speed == 0:
                    a += 1
                    self.hi= 9
                    self.delText()
                elif self.speed == 1:
                    a += 1
                    self.hi = 5
                    self.delText()
                else :
                    a += 1
                    self.hi = 2
                    self.delText()

    def delText(self):
        k=0
        if xyList != []:
            self.labels[xyList[0][0]][xyList[0][1]].setText('')
            del(wordList[0])
            #self.lifeEdit.setText('k')
            del(xyList[0])
            k += 1

    def clear(self):
        for i in range(2):
            for j in range(2):
                self.labels[i][j].setText('')
        xyList.clear()
        wordList.clear()
        self.s = 0
        self.score.setText(str(self.s))


    def toggleButton(self, state):
        if state:
            self.flag=True
            self.chaeyeon.gameStart(self.lang.currentIndex(),
                               self.level.currentIndex())
            self.test(self.level.currentIndex())
            self.edit.setEnabled(True)
            self.btn.setText('End')
            self.lang.setEnabled(False)
            self.level.setEnabled(False)
            self.setText()
            window2.close()

        else:
            self.flag=False
            self.chaeyeon.gameOver()
            self.edit.setEnabled(False)
            self.btn.setText('Start')
            self.lang.setEnabled(True)
            self.level.setEnabled(True)
            window3 = make.Ass()
            window3.hi(self.level.currentText(), self.s, self.lang.currentText())
            window2.show()
            self.clear()

    def keyPressEvent(self, e):
        self.edit.setFocus()
        if e.key() == Qt.Key_Return:
            self.delword(self.edit.text())
            self.edit.setText('')

    def delword(self,strr):
        i = 0

        for w in wordList[:]:
            if strr == w:
                del(wordList[i])
                self.labels[xyList[i][0]][xyList[i][1]].setText('')
                del (xyList[i])
                self.s += 1
                k=str(self.s)
                self.score.setText(k)
                break
            else:
               i+=1

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    type = Window()
    type.show()
    window2 = make.MyWindow()
    sys.exit(app.exec_())