n = int(input())
l = []
for _ in range(n):
    l.append(input())
c = 1
for i in range(n-1):
    if l[i] == l[i+1]:
        continue
    c = c+1

print(c)
