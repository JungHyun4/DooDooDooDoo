from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
import random
import record

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
        self.wordLabels = [[x for x in range(3)], [x for x in range(3)], [x for x in range(3)], [x for x in range(3)],
                       [x for x in range(3)]]

        for i in range(3):
            for j in range(3):
                self.wordLabels[i][j] = QLabel('')
                grid.addWidget(self.wordLabels[i][j], i, j)

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
        self.scoreLabel = QLabel('Score:')
        self.score = 0
        self.scoreEdit = QLineEdit(str(self.score))
        self.scoreEdit.setReadOnly(True)
        self.hbox4.addWidget(self.scoreLabel)
        self.hbox4.addWidget(self.scoreEdit)

        # 목숨 칸
        self.LifeLabel = QLabel('Life:')
        self.life = ' 😯 😯 😯 😯 😯 '
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

    def setText(self):
        if self.flag :
            if self.lang.currentIndex() == 1:
                words = ["hi", "car", "tt", "apple"]
            else:
                words = ["안녕", "하세요", "선생님", "그래"]
            x = random.randint(0,2)
            y = random.randint(0,2)
            z = random.randrange(len(words))

            if self.wordLabels[x][y].text() == '':
                self.wordLabels[x][y].setText(words[z])
                wordList.append(words[z])
                xyList.append([x,y])

            threading.Timer(1, self.setText).start()

    def speedControl(self, l):
        if self.flag :
            self.lv = l
            if self.lv == 0:
                self.speed = 9
                self.delText()
            elif self.lv == 1:
                self.spped = 5
                self.delText()
            else :
                self.speed = 2
                self.delText()

    def delText(self):
        if self.flag:
            threading.Timer(self.speed, self.delText).start()
            if xyList != []:
                self.wordLabels[xyList[0][0]][xyList[0][1]].setText('')
                del(wordList[0])
                #self.lifeEdit.setText('k')
                del(xyList[0])

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.wordLabels[i][j].setText('')
        xyList.clear()
        wordList.clear()
        self.score = 0
        self.scoreEdit.setText(str(self.score))

    def toggleButton(self, state):
        if state:
            self.flag=True
            self.speedControl(self.level.currentIndex())
            self.edit.setEnabled(True)
            self.btn.setText('End')
            self.lang.setEnabled(False)
            self.level.setEnabled(False)
            self.setText()
            recordWindow.close()

        else:
            self.flag=False
            self.edit.setEnabled(False)
            self.btn.setText('Start')
            self.lang.setEnabled(True)
            self.level.setEnabled(True)
            info = record.Info()
            info.info(self.level.currentText(), self.score, self.lang.currentText())
            recordWindow.show()
            self.clear()

    def keyPressEvent(self, e):
        self.edit.setFocus()
        if e.key() == Qt.Key_Return:
            self.delword(self.edit.text())
            self.edit.setText('')

    def delword(self,dword):
        i = 0
        for w in wordList[:]:
            if dword == w:
                del(wordList[i])
                self.wordLabels[xyList[i][0]][xyList[i][1]].setText('')
                del (xyList[i])
                self.score += 1
                self.scoreEdit.setText(str(self.score))
                break
            else:
               i+=1

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    type = Window()
    type.show()
    recordWindow = record.MyWindow()
    sys.exit(app.exec_())