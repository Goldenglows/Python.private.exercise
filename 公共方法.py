#使用两个列表分别存储销售额和成本
sale = [52000.00,51000.00,48000.00]
cost = [46800.00,45900.00,43200.00]
#用zip将两个列表进行合成
zipped = zip(sale,cost)
#遍历2的结果
print(list(zipped))
#输出每月的利润
print('月销售利润为:')
for i in range(3):
    print(sale[i]-cost[i])
