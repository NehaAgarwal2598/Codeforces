n = int(input())
t = list(map(int, input().split()))
c=1
l=[]
step=1
for i in range(n-1):
    if t[i]+1 != t[i+1]:
        c +=1
        l.append(step)
        step=0

    step = step+1

l.append(step)
print(c)
for i in l:
    print(i, end=' ')

    
