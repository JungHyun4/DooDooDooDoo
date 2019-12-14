from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
import time
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        #self.test()


    def initUI(self):

        # GRID
        grid = QGridLayout()
        self.labels = [[x for x in range(5)], [x for x in range(5)], [x for x in range(5)], [x for x in range(5)],
                       [x for x in range(5)]]

        for i in range(5):
            for j in range(5):
                self.labels[i][j] = QLabel('')
                grid.addWidget(self.labels[i][j], i, j)

        self.labels[0][0].setText("asd")

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
        self.lang.addItem('한글')
        self.lang.addItem('영어')
        self.lang.setCurrentIndex(0)
        self.hbox2.addWidget(self.lang)

        # 난이도
        self.level = QComboBox()
        self.level.addItem('초보자')
        self.level.addItem('중급자')
        self.level.addItem('전문가')
        self.level.setCurrentIndex(0)
        self.hbox2.addWidget(self.level)

        # 단어 입력창
        self.edit = QLineEdit()
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
        self.life = QLineEdit('😯 😯 😯 😯 😯')
        self.life.setReadOnly(True)
        self.hbox4.addWidget(self.LifeLabel)
        self.hbox4.addWidget(self.life)

        # 게임 시작버튼
        self.btn = QPushButton('게임시작')
        self.btn.setCheckable(True)
        #self.btn.toggled.connect(self.toggleButton)
        self.hbox2.addWidget(self.btn)

        self.vbox1.addLayout(self.hbox4)
        self.vbox1.addLayout(self.hbox2)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(grid)
        self.vbox.addLayout(self.vbox1)
        self.setLayout(self.vbox)
        self.setGeometry(300,300,700,700)
        self.setWindowTitle('test')
        self.show()
        self.test()

    def setText(self):
        words=["hi","car","tt","apple"]
        x = random.randint(0,4)
        y = random.randint(0,4)
        z = random.randrange(len(words))
        list=[]
        if self.labels[x][y].text() == '':
            self.labels[x][y].setText(words[z])
            list.append([x,y])
        print('hi')
        threading.Timer(2,self.setText).start()

    def test(self):
        a = 0
        if a == 0 :
            self.delText()
            a +=1
            print(a)

    def delText(self):
          for i in range(5):
               for j in range(5):
                   if self.labels[i][j].text() != '':
                       self.labels[i][j].setText('')
                       print('bye')
                       break
          threading.Timer(9,self.delText).start()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    type = Window()
    type.setText()
    type.show()
    sys.exit(app.exec_())