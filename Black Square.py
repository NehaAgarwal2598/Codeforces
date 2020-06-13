a = list(map(int, input().split()))
s = input()
c=0
for i in s:
    j = int(i)-1
    c +=a[j]

print(c)
