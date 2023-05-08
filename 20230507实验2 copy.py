def get_index1(lst=None, item=''):
    tmp = []
    tag = 0
    for i in lst:
        if i == item:             
            tmp.append(tag)
        tag += 1
    return tmp

list = []
target,n=map(int,input().split())
a=input().split(" ")
al=[int(a[i]) for i in range(n)]
ai=get_index1(list, target)
at=[ai[0],ai[len(ai)-1]]
print(" ".join(str(i) for i in at))