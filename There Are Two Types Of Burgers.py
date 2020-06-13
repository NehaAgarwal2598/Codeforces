t = int(input())
for _ in range(t):
    amt = 0
    b, p, f = list(map(int, input().split()))
    h, c = list(map(int, input().split()))

    b = b//2
    if b >= f:
        amt = f*c
        b = abs(b-f)


    elif b < f and b!=0:
        amt = b*c
        b = 0

    if b!=0 and(b<=p or b>p):
        amt = 
