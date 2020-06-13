from collections import Counter
n = int(input())
l = [0]*n
for _ in range(n):
    e = input()
    if e in l:
        print("Yes")
    else:
        print("No")
    l.append(e)
