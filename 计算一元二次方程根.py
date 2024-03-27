import math

#输入
a = float(input("请输入a: "))
b = float(input("请输入b: "))
c = float(input("请输入c: "))

#当a等于0时考虑两种情况
if a == 0:
    if b != 0:
        x = -c / b
        print("方程的实数根为:", round(x, 2))
    else:
        print("方程没有实数根")
else:
    #计算delta，并判断其和0的关系
    de = b**2 - 4*a*c
    #delta大于0则有两个根
    if de > 0:
        x1 = (-b + math.sqrt(de)) / (2*a)
        x2 = (-b - math.sqrt(de)) / (2*a)
        print("方程的实数根为:", round(x1, 2), "、", round(x2, 2))
    #delta等于0只有一个根
    elif de == 0:
        x = -b / (2*a)
        print("方程的实数根为:", round(x, 2))
    #delta小于0没有实数根
    else:
        print("方程没有实数根")
