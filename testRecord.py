import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from record_test import MyWindow
import unittest

class TestRecord(unittest.TestCase):
    def setUp(self):
        app=QApplication(sys.argv)
        self.m = MyWindow()

    def tearDown(self):
        pass

    def testshowScoreDB(self,):
        self.assertEqual(self.m.label.text(),'Name : leejung , Language : korr , Level : expert , Score : 77 , \n')

if __name__ == '__main__':
    unittest.main()




    