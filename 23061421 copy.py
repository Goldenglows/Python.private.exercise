%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import numpy as np

import pandas as pd

# 读取数据
data = pd.read_csv("bankpep.csv")

# 绘制散点图
plt.scatter(data["age"], data["income"])
plt.title("银行储户客户年龄和收入关系散点图")
plt.xlabel("年龄")
plt.ylabel("收入")
plt.show()