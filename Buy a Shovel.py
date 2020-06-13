k, r = list(map(int, input().split()))
n=1
while True:
    d = n*k
    if d%10 == 0:
        print(n)
        break
    else:
        t = d%10
        if t == r:
            print(n)
            break

        else:
            n=n+1
