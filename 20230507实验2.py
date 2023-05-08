arr = input("") 
# num = [int(n) for n in arr.split()] 
print(arr)

def halfscreach(m,n,low,high): 
    mid=(low+high)//2
    if n == m[mid]:
        return mid+1
    elif low>high:
        return False
    
    elif n>m[mid]:
        return halfscreach(m,n,low+1,high)
    else:
        return halfscreach(m,n,low,high-1)
