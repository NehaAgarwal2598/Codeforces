l = list(map(int, input().split()))

mx = max(l)

for i in range(4):
    if l[i] == mx:
        continue
    print(str(mx-l[i]), end = " ")
