n = int(input())
a = list(map(int, input().split()))
i=0
c=0
while i<n:
    if a[i]>0:
        i = i+a[i]+1
    else:
        c +=1
        i=i+1

print(c)
