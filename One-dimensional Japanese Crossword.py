n = int(input())
s = input()
l = []
c=0
for i in s:
    if i=='B':
        c=c+1

    else:
        if c!=0:
            l.append(c)
            c=0
if c!=0:
    l.append(c)
print(len(l))
if len(l)>0:
    for i in l:
        print(i, end= ' ')
