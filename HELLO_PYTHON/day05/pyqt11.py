import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt11.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        # self.com = "123"
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.setRandomCom()
        
    def setRandomCom(self):
        arr9 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        for i in range(100):
            rnd = int(random()*9)
            a = arr9[rnd]
            b = arr9[0]
            
            arr9[0] = a
            arr9[rnd] = b
        self.com = arr9[0] + arr9[1] + arr9[2]
        print("self.com: ",self.com)
        
    def myclick(self):
        # print("myclick")
        mine = self.le.text()

        c1 = self.com[0:1]
        c2 = self.com[1:2]
        c3 = self.com[2:3]
        
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        s = 0
        if c1 == m1 : s += 1
        if c2 == m2 : s += 1
        if c3 == m3 : s += 1
            
        b = 0
        if c1 == m2 or c1 == m3: b += 1
        if c2 == m1 or c2 == m3: b += 1
        if c3 == m1 or c3 == m2: b += 1
        
        str_new = mine + "\t" + str(s) + "S" + str(b) + "B" + "\n";
        str_old = self.pte.toPlainText()
        
        self.pte.setPlainText(str_old+str_new)
        self.le.setText("")
        
        if s == 3 :
            QMessageBox.about(self, "맞췄습니다.", mine)
             
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    