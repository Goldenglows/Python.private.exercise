def huona(arr, n, x):
    p = arr[0] 
    for i in range(1, n + 1):
        p = p * x + arr[i] 
    return p

n = int(input())
x = int(input())
P = list(map(int, input().split()))

result = huona(P, n, x)

print(" ".join(str(huona(P, i, x)) for i in range(n)))
print(result)