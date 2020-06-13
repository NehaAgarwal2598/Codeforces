n = int(input())
a = list(map(int, input().split()))

sm = sum(a)//(n//2)
l = []
for i in range(n):
    for j in range(i+1, n):
        if a[i]+a[j] == sm and i+1 not in l:
            l.append(i+1)
            l.append(j+1)
            break

for i in range(0,len(l), 2):
    print(l[i], l[i+1])
