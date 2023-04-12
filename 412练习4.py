print("输入一个大于2的自然数:")
num=int(input())
n=num
list=[]
# if n < 2:
#     exit()
# else:
while num>2:   
    for i in range(2,n):
        if n%i== 0:
            n-=1
            break
        else:
            list.insert(0,n)
            n-=1
list.insert(0,2)
if n in list:
    del list[list.index(n)]
print( list)


# prime_num=[]
# n=int(input())
# num=n
# while num>2:        
#      for i in range(2,num):
#         if num%i==0:             
#             num-=1  #判断素数，若不为素数if语句执行并自减1
#             break   #退出for循环后执行while语句
#      else:         #若为素数if语句不执行，执行else语句
#         prime_num.insert(0,num)
#         num-=1     #else不执行for循环，if执行               
# prime_num.insert(0,2)
# if n in prime_num:
#     del prime_num[prime_num.index(n)]   #查找并删除输入的数字
# print( prime_num)
