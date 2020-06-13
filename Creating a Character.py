t = int(input())
for _ in range(t):
    cnt = 0
    a, b, c = list(map(int, input().split()))
    if a <= b and c>(b-a):
        d = b-a
        a = a+d+1
        nb = b
        c = c-d-1

    else:
        a = a+c//2
        nb = b+c//2
        c = c//2
    
    d = a+c
    while d> nb and nb<d+1:
        d= d-1
        nb=nb+1
        cnt +=1
        

    print(cnt)
        
