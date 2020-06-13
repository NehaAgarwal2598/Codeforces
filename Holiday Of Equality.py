n = int(input())
a = list(map(int, input().split()))
mx = max(a)
c=0
for i in a:
    c = c+(mx-i)

print(c)
