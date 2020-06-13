n, k = list(map(int, input().split()))
ar = list(map(int, input().split()))
c=0
for i in ar:
    if i > k:
        c = c+2

    else:
        c = c+1

print(c)
