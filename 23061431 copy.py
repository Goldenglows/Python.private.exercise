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
data_sorted = data.sort_values(by="Length (km)", ascending=False)

# 提取各国的现状和规划里程数据
present_data = data_sorted[["Country/Territory", "Present Length"]]
plan_data = data_sorted[["Country/Territory", "Planned Length"]]

# 绘制堆叠柱状图
fig, ax = plt.subplots()
ax.bar(data_sorted["Country/Territory"], present_data["Present Length"], color="blue", label="现状")
ax.bar(data_sorted["Country/Territory"], plan_data["Planned Length"], bottom=present_data["Present Length (km)"], color="orange", label="规划")
plt.title("各国运营里程现状和发展堆叠柱状图")
plt.xlabel("国家/地区")
plt.ylabel("里程")
plt.xticks(rotation=90)
plt.legend()
plt.show()