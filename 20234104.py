print('请输入一个1000以内的正整数：')
num = int(input())
#设置一个函数判断是不是质数
def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True
#判断输入的值是否符合标准
if num > 1000:
    print('输入有误')
    exit()
else:
    #将质数放在一个列表中
    num_isprime = [n for n in range(2,num) if isprime(n)]
    #设置一个计数器
    flag = 0
    #设置循环，如果num减去一个质数等于另一个质数，则让计数器加一
    for m in num_isprime:
        if (num - m) in num_isprime and m <=num - m:
            flag +=1
            
print(flag)


# num = int(input())
 
# def isPrime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     else:
#         return True
 
# primeli = [i for i in range(2,num) if isPrime(i)]
# print(primeli)
 
# primecount = 0
 
# # [2,3,5,7]
# for item in primeli:
#     if (num - item) in primeli and item <= num - item:
#         primecount += 1
 
# print(primecount)

