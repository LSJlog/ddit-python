import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from numpy import integer

form_class = uic.loadUiType("pyqt02.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        # l = QLabel("ss", self)
        
        # print("myclick")
        a = self.lbl.text()
        aa = int(a)
        aa -= 1
        self.lbl.setText(str(aa))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    