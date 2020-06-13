n = int(input())
ar = list(map(float, input().split()))
c=0
for i in range(n):
    c = c+(ar[i]/100)

print(c*100/n)
