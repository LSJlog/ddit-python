import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from numpy import integer
from random import random

form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.leMine.editingFinished.connect(self.myclick)
        
    def myclick(self):
        # print("myclick")
        
        mine = ""
        com = ""
        result = ""
        
        mine = self.leMine.text()
        
        rnd = random()
        # print("rnd: ", rnd)
        
        if rnd > 0.5:
            com = "짝"
        else:
            com = "홀"
        
        if mine == com:
            result = "승리"
        else:
            result = "패배"
        
        self.leCom.setText(com)
        self.leResult.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    