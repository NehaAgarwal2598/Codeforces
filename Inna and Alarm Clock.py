n = int(input())
l = []
for _ in range(n):
    e = list(map(int, input().split()))
    l.append(e)
c = 1
l = sorted(l)
for i in range(n-1):
    if l[i][0] != l[i+1][0]:
        c = c+1

print(c)
    
