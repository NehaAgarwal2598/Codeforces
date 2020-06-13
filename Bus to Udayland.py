n = int(input())
l=[]
for _ in range(n):
    l.append(input())
f=0
for i in l:
    if i[0:2] == 'OO' or  i[3:] == 'OO':
        l[l.index(i)] = i.replace('OO', '++',1)
        f=1
        break

if f==1:
    print("YES")
    for i in l:
        print(i)

else:
    print("NO")
