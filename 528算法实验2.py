n, k = map(int, input().split())
p = list(map(int, input().split()))

# 将萝卜数量按从大到小排序
p.sort(reverse=True)

total = sum(p)
for i in range(k):
    # 选择剩余的数量最多的堆进行运送
    half = (p[0] + 1) // 2  
    # 计算运送剩余的数量后，更新总数
    total -= p[0] - half  
    # 更新堆中的数量，重新排序
    p[0] = half  
    p.sort(reverse=True)

print(total)  



