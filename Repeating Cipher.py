n = int(input())
s = input()
i, t=0, 1
ns = ''
while i<n:
    ns = ns+s[i]
    i = i+t
    t = t+1

print(ns)
