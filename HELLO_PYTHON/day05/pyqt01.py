import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt01.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        #print("myclick")
        self.lbl.setText("Good Evening")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    