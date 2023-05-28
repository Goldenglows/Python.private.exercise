import numpy as np 

names=np.array(["王微","肖良英","方绮雯","刘旭阳","钱易铭"])
subjects=np.array(["Math","English","Python","Chinese","Art","Database","Phtsics"])
#根据学生成绩定义的数组
scores1=np.array([70,85,77,910,82,84,89],[60,64,80,75,80,92,90],[90,93,88,87,86,90,91],[80,82,91,88,83,86,80],[88,72,78,90,91,73,80])
#根据科目定义数组
scores2=np.array([70,60,90,80,88],[85,64,93,82,72],[77,80,88,91,78],[90,75,87,88,90],[82,80,86,83,91],[84,92,90,86,73],[89,90,91,80,80])

#以names为例
s=slice(2,5,2)
print(names[s])
#["方绮雯"，"钱易铭"]

n=names[2:5:2]
print(n)
#["方绮雯"，"钱易铭"]

print(names[2:])
#["方绮雯","刘旭阳","钱易铭"]

print(names[2:3])
#["方绮雯","刘旭阳"]

print(scores1[1:])
#([60,64,80,75,80,92,90],
# [90,93,88,87,86,90,91],
# [80,82,91,88,83,86,80],
# [88,72,78,90,91,73,80])

print (scores1[...,1])   
# 第2列元素
#[85,64,93,82,72]
print (scores1[1,...])   
# 第2行元素
#[60,64,80,75,80,92,90]
print (scores1[...,1:]) 
# 第2列及剩下的所有元素
# [85,64,93,82,72],
# [77,80,88,91,78],
# [90,75,87,88,90],
# [82,80,86,83,91],
# [84,92,90,86,73],
# [89,90,91,80,80]

scores1[names=='肖良英']
scores1[names=='万绮雯']

scores1[names=='肖良英'&subjects=='Math']
scores1[names=='万绮雯'&subjects=='Python']
scores1[names=='万绮雯'&subjects=='Math']
scores1[names=='肖良英'&subjects=='Python']

scores2=scores2+5

add1=np.array([3,4,5,3,6,7,2])
scores1=scores1+add1

scores1[1,1]=90

import math   
print(math.floor(scores1))

threes_arr = np.full(shape=(5,7),fill_value=3)
print(np.subtract(scores1,threes_arr))

scores1.sum(axis = 0)     

scores1[names == '王微'].mean()

names[scores1[:,subjects == 'English'].argmax()]

subjects[1]

subjects[6]

scores1[2,0]
scores1[2,2]
scores1[4,0]
scores1[4,2]

scores1[names == '王微',subjects == 'English']
scores1[names == '王微',subjects == 'Art']
scores1[names == '刘旭阳',subjects == 'English']
scores1[names == '刘旭阳',subjects == 'Art']

meansnum=np.array([names==names[x] for x in range(0,4),subjects=y for y in range(0,6)]).mean()