from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #GRID
        grid = QGridLayout()
        labels = ['']*25
        positions = [(i,j) for i in range(5) for j in range(5)]

        for position, label in zip(positions, labels):
            label = QLabel('🍎')
            grid.addWidget(label, *position)

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




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    type = Window()
    type.show()
    sys.exit(app.exec_())