a, b, c = list(map(int, input().split()))
if a==b or a+1 == b or b+1 == a:
    print(a+b+c*2)

else:
    print(min(a,b)*2+1+c*2)
    
