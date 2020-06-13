from collections import Counter
s = list(map(int, input().split()))
d = Counter(s)
print(4-len(list(d.values())))
