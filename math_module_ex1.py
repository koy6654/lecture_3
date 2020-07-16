import math as mt


def math_m(a,b):
    result = mt.pow(a,b)
    return result


print("x^y 값을 구합니다")
x = int(input("x를 입력하세요"))
y = int(input("y를 입력하세요"))

for i in range(1,y+1):
    val = math_m(x,i)
    print("{}^{} = {}". format(x,i,val))