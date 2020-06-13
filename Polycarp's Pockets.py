from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
l = max(list(c.values()))
print(l)
