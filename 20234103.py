#将集合转化为列表
num = {11,22,33,44,55,66,77,88,99,90,100,99}
num_list = list(num)
#创造一个字典和两个列表
key = {}
list_1 = []
list_2 = []
#利用循环判断每一个元素和66比较大小
for n in range(0,len(num_list)-1):
    if num_list[n] < 66:
        #如果小于66则放在列表1中
        list_1.append(num_list[n])
    else:
        #如果大于等于66则放在列表2中
        list_2.append(num_list[n])
#形成字典
num_dict = {'k1':list_1,'k2':list_2}
print(num_dict)