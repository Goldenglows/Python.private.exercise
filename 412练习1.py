list1 = [52000.00,51000.00,48000.00]
list2 = [46800.00,45900,00,43200,00]

list3 = list(zip(list1,list2))
print(list3)

for i in range (0,3):
    print(i,"月利润为：")
    print(list1[i]-list2[i])
