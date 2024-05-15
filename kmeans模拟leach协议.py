import numpy as np
import matplotlib.pyplot as plt

#定义常量
NUM_NODES = 40  #节点数量
X_BOUND = 100  #X轴边界
Y_BOUND = 100  #Y轴边界

#生成随机节点
nodes = np.random.rand(NUM_NODES, 2) * np.array([X_BOUND, Y_BOUND])

#初始化节点参数，能量 传输功率
energies = np.random.rand(NUM_NODES)
transmit_powers = np.random.rand(NUM_NODES)

from sklearn.cluster import KMeans

#定义簇的数量
NUM_CLUSTERS = 4

#使用 K-means 算法进行聚类
#KMeans: 这是 scikit-learn 库中实现的 K-means 聚类算法的类。K-means 是一种无监督学习算法，用于将数据点分成 k 个不同的组（簇），使得每个数据点都属于与其最近的簇的中心。
#n_clusters=NUM_CLUSTERS: 这是 K-means 算法的一个参数，指定要分成的簇的数量。在这个代码中，NUM_CLUSTERS 是一个预先定义好的常量，代表了要分成的簇的数量。
#random_state=0: 这是一个可选参数，用于控制随机性。在 K-means 算法中，初始的簇中心点是随机选择的。通过设置 random_state 参数，可以使得每次运行算法时得到相同的随机结果，这样有助于结果的可重复性。
#.fit(nodes): 这是调用 K-means 算法的 fit 方法，用于对数据进行聚类。nodes 是要进行聚类的数据集，通常是一个二维数组或矩阵，其中每一行代表一个数据点，每一列代表一个特征。
kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=0).fit(nodes)

#获取簇的中心点和每个节点所属的簇
cluster_centers = kmeans.cluster_centers_
cluster_labels = kmeans.labels_

#绘制节点和簇头节点
#创建一个图像窗口 大小为8 6
plt.figure(figsize=(8, 6))
#绘制散点图 节点     x            y      节点所属的簇标签来进行着色  颜色映射      图例标签
plt.scatter(nodes[:, 0], nodes[:, 1], c=cluster_labels, cmap='viridis', label='Nodes')
#         簇中心     x               y                       使用x表示簇中心 标记大小为100
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', s=100, c='red', label='Cluster Heads')
plt.title('Wireless Sensor Network with Cluster Heads')
plt.xlabel('X')
plt.ylabel('Y')
#显示图例
plt.legend()
#显示网格线
plt.grid(True)
plt.show()

#LEACH 协议的选取原则
#每个节点成为簇头节点的概率
#用于生成指定形状的随机数组，每一个元素都是0到1的随机数
probabilities = np.random.rand(NUM_NODES)

#随机选择簇头节点
cluster_heads = [i for i in range(NUM_NODES) if probabilities[i] < 0.1]

#绘制节点和簇头节点
plt.figure(figsize=(8, 6))
plt.scatter(nodes[:, 0], nodes[:, 1], c='blue', label='Nodes')
plt.scatter(nodes[cluster_heads, 0], nodes[cluster_heads, 1], marker='x', s=100, c='red', label='Cluster Heads')
plt.title('Wireless Sensor Network with LEACH Protocol')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()


