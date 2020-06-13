x1, x2, x3 = list(map(int, input().split()))
l=[]
l.append(abs(x1-x2))
l.append(abs(x1-x3))
l.append(abs(x2-x3))
c=0
c =c+min(l)

l.remove(c)
c=c+min(l)

print(c)
