n, m = list(map(int, input().split()))
s = list(input())

for _ in range(m):
    l, r, c1, c2 = list(input().split())
    l = int(l)
    r = int(r)

    for i in range(l-1,r):
        if s[i] == c1:
            s[i]=c2


print("".join(s)) 
        
        
