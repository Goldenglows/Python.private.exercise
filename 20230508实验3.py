
def amstl_num(num):
    a=num/100
    b=(num-a*100)/10
    c=num-a*100-b*10
    if(num==a**3+b**3+c**3):
        return num
    else:
        return -1
    
amstlist=[]
for i in range(100,999):
    n = len(str(i))
    sw = 0
    gw = i
    while gw > 0:
        qw = gw % 10
        sw += qw ** n
        gw //= 10
 
    if i == sw:
        amstlist.append(i)
        

print(amstlist)