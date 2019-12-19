from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
import time
import random
import record_test
from window_test import Window
import unittest
import sys

class TestWindow(unittest.TestCase):

    def setUp(self):
        app = QApplication(sys.argv)
        self.t1 = Window()

    def tearDown(self):
        pass

    def testsetText(self):
        self.t1.setText(1, 0, 2)
        self.assertEqual(self.t1.labels[1][0].text(),'topic')
        self.t1.setText(0, 0, 3)
        self.assertEqual(self.t1.labels[0][0].text(), 'apple')
        self.t1.setText(1, 1, 1)
        self.assertEqual(self.t1.labels[1][1].text(), 'car')

    def testdelText(self):
         self.t1.delText()
         self.assertEqual(self.t1.labels[0][0].text(), "")
         self.t1.delText()
         self.assertEqual(self.t1.labels[1][1].text(), "")

    def testdelword(self):
        self.t1.delword('topic')
        self.assertEqual(self.t1.labels[1][0].text(),'')

if __name__ == '__main__':
    unittest.main()




