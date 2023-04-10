#print('请输入一组整数：')
#tup = tuple(map(int, input().split()))
#for n in range (0,len(tup)):
    #print(n+':'+tup.count(n))
num_line = input("输入一组整数：")
#创建一个列表，存放输入的整数组
num_strs = num_line.split()
num_list = []
for n in num_strs:
    num_list.append(int(n))
#创建一个字典
num_dict = {}
#字典中出现一次就为1，如果多出现一次，就加一
for n in num_list:
    if n in num_dict:
        num_dict[n] = num_dict[n] + 1
    else:
        num_dict[n] = 1
print("各个数字出现的次数如下：")
#输出：
for n,m in num_dict.items():
    print(n,':',m,'次')