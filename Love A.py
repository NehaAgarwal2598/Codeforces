from collections import Counter

s = input()
d = Counter(s)
c = 0
#print(d['a'])
#print(d)
for i in d:
    if i == 'a':
        continue
    c = c+d[i]
    
#print(c)
if c < d['a']:
    print(len(s))

elif c == d['a']:
    print(len(s)-1)
    
else:
    print(len(s)-(c-d['a'])-1)
