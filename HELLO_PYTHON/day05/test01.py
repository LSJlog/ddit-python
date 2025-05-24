# 한번에 2단에서 9단

# txt = ""

# for i in range(9, 2, -1):
#     # 9 7 3 2 - 9
#
#     if (i % 9 == 0) or (i % 7 == 0) or (i % 3 == 0) or (i % 2 == 0):
#         for j in range(1, 9+1):
#             txt = "{}*{}={}".format(i,j,i*j)
#             print(txt)
#         print("")

def showdan(dan):
    print("{}*{}={}".format(dan,1,dan*1))
    print("{}*{}={}".format(dan,2,dan*2))
    print("{}*{}={}".format(dan,3,dan*3))
    print("{}*{}={}".format(dan,4,dan*4))
    print("{}*{}={}".format(dan,5,dan*5))
    print("{}*{}={}".format(dan,6,dan*6))
    print("{}*{}={}".format(dan,7,dan*7))
    print("{}*{}={}".format(dan,8,dan*8))
    print("{}*{}={}".format(dan,9,dan*9))

showdan(9)
showdan(7)
showdan(3)
showdan(2)
