import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbn.clicked.connect(self.myclick)
        
    def myclick(self):
        #print("myclick")
        dan = int(self.le.text())
        
        txt = ""
        
        for i in range(1,9+1) :
            txt += "{}*{}={}\n".format(dan,i,dan*i) 
            
        self.pte.setPlainText(txt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    