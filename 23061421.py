%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import numpy as np

import pandas as pd

# 读取数据
data = pd.read_csv("bankpep.csv")

# 绘制直方图
plt.hist(data["age"], bins=10, edgecolor="black")
plt.title("银行储户客户年龄分布直方图")
plt.xlabel("年龄")
plt.ylabel("频数")
plt.show()