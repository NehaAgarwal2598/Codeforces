m, n = list(map(int, input().split()))
#if (n%2 == 0 and m%2 == 0) or (m%2 == 0 and n == 1) or (m%2 == 0):
if  m%2 == 0:
    sm = (m//2)*n

elif m == 1:
    sm = n//2

else:
    sm = (m//2)*n+(n//2)

print(sm)
    
    
