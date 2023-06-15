%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import numpy as np

import pandas as pd

# 读取数据
data = pd.read_csv("high-speed rail.csv")

# 绘制饼图
plt.pie(data["Length (km)"], labels=data["Country/Territory"], autopct="%1.1f%%",
        colors=['#ff6666','#ffff66','#ff99ff','#ffb366','#66ffd9','#66b3ff','#b3ff66','#9999ff','#cc3300'])

# 标注China扇形离开中心点
plt.subplots_adjust(left=0.2, bottom=0.2, right=1)
plt.title("世界各国高铁运营里程占比饼图")
plt.legend(loc="lower right", bbox_to_anchor=(1.5, 0))
plt.show()