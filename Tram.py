k, n, w = list(map(int, input().split()))
b = 0
m = w*(w+1)//2*k
if n-m >=0:
    print("0")
else:
    print(m-n)

