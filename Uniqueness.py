from collections import Counter
n = int(input())
a = list(map(int, input().split()))

d = Counter(a)
print(d)
c = 0
for i in d:
    c = c+(d[i]-1)
    print(d[i], c)
print(c)
