n = int(input())
c=0
for _ in range(n):
    p, q = list(map(int, input().split()))
    if q-p >=2:
        c= c+1

print(c)
