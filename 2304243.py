#4

#实现不区分大小的 字符串排序
list=['bob','about','Zoo','Credit']
list_sort=sorted(list,key=str.lower)
print(list_sort)

#根据长度排序
list_len=sorted(list,key=len)
print(list_len)