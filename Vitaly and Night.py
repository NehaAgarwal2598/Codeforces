n, m = list(map(int, input().split()))
c=0
for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(0,2*m,2):
        if a[i]==1 or a[i+1]==1:
            c +=1


print(c)
    
