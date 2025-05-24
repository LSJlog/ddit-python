def showDan(dan):
    # print(str(dan) + "*" + str(1) + "=" + str(dan*1))
    # print(str(dan) + "*" + str(1) + "=" + str(dan*2))
    
    dan = int(dan)
    
    for i in range(1,9+1):
        mul = dan * i
        print("{} * {} = {}".format(dan, i, str(mul)))
        
    # print("{}*{}={}".format(dan,1,dan*1))
    # print("{}*{}={}".format(dan,2,dan*2))

showDan(5)

