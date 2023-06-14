%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import numpy as np

import pandas as pd

# 读取数据
data = pd.read_csv("population.csv")

# 根据年份对新出生人数进行分组并求和，并将结果存储在一个Series对象中
year_data = data.groupby("year")["born"].sum()

# 绘制折线图
plt.plot(year_data.index, year_data.values)
plt.title("中国2013到2019年新出生总数折线图")
plt.xlabel("年份")
plt.ylabel("中国人口新出生总数")
plt.show()