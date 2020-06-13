t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    a=[]
    for i in range(n):
        l = list(map(int, input().split()))
        a.append(l)
    x = x-a[0][0]+a[0][1]
    c=1
    flag = 0
    for i in range(1,n):
        while x < a[i][1]:
            x = x-min(x, a[i][0])
            c= c+1
            if x<=0 :
                print(c)
                flag =1
                break
            x = x + a[i][1]
        #print(x)
        #print(c)
        if flag ==0:
            print("-1")
            break
        else:
            x = x= min(x, a[i][0])
        
        

    
