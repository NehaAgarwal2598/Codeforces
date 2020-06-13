w, h, k = list(map(int, input().split()))
c=0
for i in range(k):
    c = c+ ( (h-4*i)*2 +( w - 2-4*i)*2)

print(c)
