import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from numpy import integer
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        # print("myclick")
        arr = [
            1, 2, 3, 4, 5, 6, 7, 8, 9 ,10,
            11, 12, 13, 14, 15,16, 17, 18, 19 ,20,
            21, 22, 23, 24, 25, 26, 27, 28, 29 ,30,
            31, 32, 33, 34, 35, 36, 37, 38, 39 ,40,
            41, 42, 43, 44, 45
        ]
        
        for i in range(1000):
            rnd = int(random()*45)
            a = arr[0]
            b = arr[rnd]
        
            arr[0] = b
            arr[rnd] = a
        
        self.te1.setText(str(arr[0]))
        self.te2.setText(str(arr[1]))
        self.te3.setText(str(arr[2]))
        self.te4.setText(str(arr[3]))
        self.te5.setText(str(arr[4]))
        self.te6.setText(str(arr[5]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    