
list=[1,2,3,4,5,6,7,8,9,10]
print("初始列表："+str(list))
i=1

while True:
    list.append(list[0])
    list.append(list[1])
    del list[0]
    del list[0]
    list_pop=list.pop(0)
    print("第"+str(i)+"轮："+str(list)+str(list_pop))
    i+=1
    if len(list)==1:
        break
    






# def listcut(list=[]):
#     list_new=list[3:]+list[0:2]
#     return list_new

# list=[1,2,3,4,5,6,7,8,9,10]
# print("初始列表："+str(list))

# for i in range(9):

#     print("第"+str(i+1)+"轮："+str(listcut(list))+str(list[2]))

# list=[1,2,3,4,5,6,7,8,9,10]
# print("初始列表："+str(list))
# for i in range(9):
#     list2=list
#     list1=list[(i+1)*3:]+list[0:1]
#     list2_pop=list2.pop(2)
#     print("第"+str(i+1)+"轮："+str(list1)+str(list2_pop))
