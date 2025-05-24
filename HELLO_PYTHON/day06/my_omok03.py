import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QIcon, QSize
from conda.common._logic import FALSE
from anyio._backends._asyncio import sleep
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("my_omok03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.flag_dol = True
        # 변수명의 중요성
        # self.flag_ing = True

        self.flag_over = False
        self.arr2D=[
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
        ]
        self.pbs=[]
        
        self.setupUi(self)
        self.pb.clicked.connect(self.myreset)

        for i in range(19):
            for j in range(19):
                temp = QPushButton('', self)
                temp.setToolTip("{},{}".format(i,j))
                temp.setIcon(QIcon("0.png"))
                temp.setIconSize(QSize(40, 40))
                temp.setGeometry(j*40, i*40, 40, 40)
                temp.clicked.connect(self.myclick)
                self.pbs.append(temp)
                
        self.myrender()
        
    def myreset(self):
        for i in range(19):
            for j in range(19):
                self.arr2D[i][j]=0
        
        self.myrender()
        self.flag_dol = True
        self.flag_over = False
        
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0:
                    self.pbs[i*19+j].setIcon(QIcon("0.png"))
                if self.arr2D[i][j] == 1:
                    self.pbs[i*19+j].setIcon(QIcon("1.png"))
                if self.arr2D[i][j] == 2:
                    self.pbs[i*19+j].setIcon(QIcon("2.png"))
         
    def myclick(self):
        if self.flag_over == True:
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0 :
            return
        
        stone = -1
        
        if self.flag_dol:
            self.arr2D[i][j]=1
            stone = 1
        else:
            self.arr2D[i][j]=2
            stone = 2
        
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        le = self.checkLE(i,j,stone)
        ri = self.checkRI(i,j,stone)
        
        ul = self.checkUL(i,j,stone)
        ur = self.checkUR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        # print(up,dw,le,ri, ul,ur,dl,dr)
        
        d1 = up + dw + 1
        d2 = ul + dr + 1
        d3 = le + ri + 1
        d4 = ur + dl + 1
        
        self.myrender()
        
        if d1==5 or d2==5 or d3==5 or d4==5:
            if self.flag_dol:
                QMessageBox.about(self,'오목', '흑돌승리')
                self.flag_over = True
            else:
                QMessageBox.about(self,'오목', '백돌승리')
                self.flag_over = True
                
        self.flag_dol = not self.flag_dol
    
    
    def checkUP(self,i,j,stone):#위
        cnt=0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def checkDW(self,i,j,stone):#아래
        cnt=0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLE(self,i,j,stone):#왼쪽
        cnt=0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRI(self,i,j,stone):#오른쪽
        cnt=0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUL(self,i,j,stone):#
        cnt=0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUR(self,i,j,stone):#
        cnt=0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDL(self,i,j,stone):#
        cnt=0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDR(self,i,j,stone):#
        cnt=0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    