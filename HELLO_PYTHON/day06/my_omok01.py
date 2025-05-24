import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QIcon, QSize
from conda.common._logic import FALSE

form_class = uic.loadUiType("my_omok01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.flag_dol = True
        self.setupUi(self)
        self.pb.clicked.connect(self.reset)

        for i in range(10):
            for j in range(10):
                temp = QPushButton('', self)
                temp.setIcon(QIcon("0.png"))
                temp.setIconSize(QSize(40, 40))
                temp.setGeometry(j*40, i*40, 40, 40)
                temp.clicked.connect(self.myclick)
        
    def myclick(self):
        if self.flag_dol == True : 
            self.sender().setIcon(QIcon("1.png"))
        else :
            self.sender().setIcon(QIcon("2.png"))
            
        self.flag_dol = not self.flag_dol
        
        # self.btn1.setIcon(QIcon("1.png"))

    def reset(self):
        print("reset")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    