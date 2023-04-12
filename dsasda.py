print("输入一个大于2的自然数:")
n=int(input())
num=n
listnum=[]
#进入循环判断是不是大于2
while num>2:
     #判断num是不是质数，接下来判断比num小比2大的数没有质数
     # 有则直接放入之前定义好的列表中        
     for i in range(2,num):
        if num%i==0:             
            num-=1 
            break  
     else:        
        listnum.insert(0,num)
        num-=1                  
listnum.insert(0,2)
#最后需要删除输入的那个数值
if n in listnum:
    del listnum[listnum.index(n)]   
print( listnum)
