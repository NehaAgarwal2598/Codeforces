n = int(input())
den = list(map(int, input().split()))
c = 0
while n!=0:
    mx = 0
    for i in den:
        if i >= mx and i <= n:
            mx = i
            d = n//i

    c = c+d
    n = n-(mx*d)
print(c)
