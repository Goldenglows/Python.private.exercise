%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import numpy as np

import pandas as pd

# 读取数据
data = pd.read_csv("bankpep.csv")

# 根据区域分组并计算平均收入
reg = data.groupby("region")["income"].mean()

# 绘制柱状图
reg.plot(kind="bar", color="blue", edgecolor="black")
plt.title("银行储户按区域展示平均收入柱状图")
plt.xlabel("区域")
plt.ylabel("平均收入")
plt.show()