%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import numpy as np

import pandas as pd

# 读取数据
data = pd.read_csv("population.csv")

# 根据年份对新出生男孩数和女孩数进行分组并求和，并将结果存储在一个DataFrame对象中
year_data = data.groupby("year")["boy", "girl"].sum()

# 绘制柱形图
year_data.plot(kind="bar", stacked=True)
plt.title("中国2013到2019年新出生男女孩数柱形图")
plt.xlabel("年份")
plt.ylabel("人数")
plt.show()