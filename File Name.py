n = int(input())
s = input()
c=0
l=[]
for i in s:
    if i == 'x':
        c +=1
    else:
        if c>=3:
            l.append(c)
        c=0
if c>=3:
    l.append(c)

print(sum(l)-2*len(l))
