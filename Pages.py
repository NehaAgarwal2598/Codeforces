n, p, k = list(map(int, input().split()))
l = []
i = 0
e = 0
while (i <= k*2 and e<n):
    e = p-k+i
    if e > 0:  
        l.append(e)
    i = i+1

if l[0] > 1:
    print('<<', end = ' ')
    
for i in l:
    if i == p:
        i = '('+str(i)+')'
    print(i, end = ' ')
    
if l[len(l)-1] < n:
    print('>>')

