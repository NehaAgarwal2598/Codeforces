n = int(input())
l=[]
for _ in range(n):
    a = list(map(int, input().split()))
    l.append(a)

sm = 0
for i in range(n):
    if i!=(n//2):
        sm = sm +l[i][i]+l[n-i-1][i]+l[i][n//2]+l[n//2][i]


sm +=l[n//2][n//2]

print(sm)


