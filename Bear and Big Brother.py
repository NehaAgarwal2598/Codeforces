lim, bob = list(map(int,input().split()))
c = 0
while lim <= bob:
    lim = lim*3
    bob = bob*2
    c = c+1

print(c)
