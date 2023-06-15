%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import numpy as np

import pandas as pd

# 读取数据
data = pd.read_csv("high-speed rail.csv")

# 将中国的行数据里程标记为"Longest"
data.loc[data["Country/Territory"] == "China", "Length"] = "Longest"

# 按照里程从高到低排序
data_sorted = data.sort_values(by="Length", ascending=False)

# 绘制柱状图
plt.bar(data_sorted["Country/Territory"], data_sorted["Length"], color="blue", edgecolor="black")
plt.title("世界各国高铁运营里程柱状图")
plt.xlabel("国家/地区")
plt.ylabel("里程")
plt.xticks(rotation=90)
plt.show()