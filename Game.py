n = int(input())
a = list(map(int, input().split()))
t = 1
k = len(a)
while t < k:    
    if t%2 != 0:
        a.remove(max(a))

    elif t%2 == 0:
        a.remove(min(a))
    t = t+1
print(a[0])
