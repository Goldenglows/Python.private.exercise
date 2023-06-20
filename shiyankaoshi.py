1.
#实现列表反向
alist.reverse()
print(alist)
#将列表中元素按升序排列
alist.sort()
print(alist)
#删除列表中索引为2的元素
del alist[2]
print(alist)
#添加元素`15`
alist.append(15)
print(alist)
#判断元素`4`是否在列表alist中
4 in alist

2.
#创建字典a
a = {'cows':1,'dogs':5,'cats':3}

#查询字典a中是否有键‘rabbit’,如没有返回None；
a.get('rabbit')

#输出字典a中所有的键值对
for key,value in a.items():
    print(key,value)

3.
import random

def panduan(values):
    for value in values:
        if value > 10:
            return value

values = [random.randint(1,13) for i in range(8)]
print("随机生成了：", values)

a = panduan(values)
if a is not None:
    print("第一个大于10的元素为：", a)
else:
    print("列表中没有大于10的元素")


4.
alist = [10, 21, 4, 7, 12]
squares = [x**2 for x in alist if x <= 10]

alist = [10, 21, 4, 7, 12]
adict = {x: x**2 for x in alist}

5.
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

6.

import numpy as np
x = np.array([1, 2, 3])

arr1 = np.zeros((2, 3))
arr2 = np.ones((3, 2))
arr3 = np.random.rand(3, 2)
arr4 = np.arange(2.0, 3.0, 0.1)
arr5 = np.linspace(1.0, 4.0, 6)

7.
import numpy as np

# 创建多维数组 a 和 b
a = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
b = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])

# 沿着行方向合并 a 和 b
c = np.concatenate((a, b), axis=0)

print(c)


8.

import numpy as np

arr = np.zeros((10, 10))
arr[0, :] = 1
arr[-1, :] = 1
arr[:, 0] = 1
arr[:, -1] = 1

print(arr)

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
B = np.array([[1, 2], [3, 4], [5, 6]])

C = np.dot(A, B)

print(C)

import numpy as np

x = np.arange(10) ** 3

# 输出数组x中索引为2的元素
print(x[2])

# 输出数组x中第二个至第四个元素(数组从第一个元素开始)
print(x[1:4])

# 将数组x中的索引为奇数的元素设为-1,并输出(数组索引从0开始)
x[1::2] = -1
print(x)

# 将数组x进行逆序并输出
y = x[::-1]
print(y)


9.
import numpy as np

# 创建多维数组并赋值
arr = np.random.normal(loc=10, scale=5, size=(100, 200))
print(arr)

#计算均值和方差：
import numpy as np

# 创建多维数组并赋值
arr = np.random.normal(loc=10, scale=5, size=(100, 200))

# 计算均值和方差
mean = np.mean(arr)
var = np.var(arr)

print("均值: ", mean)
print("方差: ", var)

#提取前200个数据并绘制直方图：
import numpy as np
import matplotlib.pyplot as plt

# 创建多维数组并赋值
arr = np.random.normal(loc=10, scale=5, size=(100, 200))

# 提取前200个数据
data = arr[:200].flatten()

# 绘制直方图
plt.hist(data, bins=50)
plt.show()