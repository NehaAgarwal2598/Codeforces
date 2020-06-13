n = int(input())
l={}
for i in range(n):
    a, b, c, d = list(map(int,input().split()))
    l.update({i+1:(a+b+c+d)/4})

mark = l[1]
l = sorted(l.values(), reverse=True)
print(l.index(mark)+1)
