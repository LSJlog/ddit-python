import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt10.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def getStar(self,cnt):
        ret = ""
        for i in range(0,cnt):
            ret += "*"
        ret += "\n"
        return ret
        
    def myclick(self):
        a = int(self.le1.text())
        b = int(self.le2.text())
        
        txt = ""
        
        for i in range(a, b+1):
            txt += self.getStar(i)
        
        self.te.setText(txt)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    