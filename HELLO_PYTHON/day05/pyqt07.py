import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbn.clicked.connect(self.myclick)
        
    def myclick(self):
        #print("myclick")
        a = int(self.le1.text())
        b = int(self.le2.text())
        c = int(self.le3.text())
        
        sum = 0
        for i in range(a, b+1) :
            if i % c == 0 :
                sum += i
        
        self.le4.setText(str(sum))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    