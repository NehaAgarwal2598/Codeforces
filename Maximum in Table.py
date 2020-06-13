n = int(input())
l = [1 for i in range(n)]
for i in range(n-1):
    for j in range(1,n):  
        l[j] = l[j-1]+l[j]
print(l[n-1])
