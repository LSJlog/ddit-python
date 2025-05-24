# 홀/짝을 입력하시오
# 나 : 홀
# 컴 : 홀
# 결과 : 승리

import random


# 주석
rnd = random.randrange(1,3)
#print(rnd)

if rnd == 1:
    rnd = "홀"
else :
    rnd = "짝"

a = input("홀/짝을 입력하시오: ")

if a == rnd :
    print("나 : " + a)
    print("컴 : " + rnd)
    print("승리")
else : 
    print("나 : " + a)
    print("컴 : " + rnd)
    print("패배")

# 풀이
# mine = ""
# com = ""
# result = ""
#
# mine = input("홀/짝을 입력하시오")
# rnd = random()
# if rnd > 0.5:
#     com = "홀"
# else:
#     com = "짝"
#
# if mine == com:
#     result = "승리"
# else:
#     result = "패배"
#
# print("나: ", mine)
# print("컴: ", com)
# print("결과: ", result)
print("바보", end="\t")
print("천재")
