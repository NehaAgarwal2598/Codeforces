n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
c = 0
for i in range(0,n,2):
    c = c + a[i+1]-a[i]
print(c)
