from collections import Counter
n = int(input())
a = list(map(int,input().split()))
d = Counter(a)
if d[1] >0:
    print("HARD")

else:
    print("EASY")
