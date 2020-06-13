from collections import Counter

s = input()
find = 'nineteen'

d = Counter(s)
df = Counter(find)
l = []
for i, ele in enumerate(df):
    l.append(d[ele]//df[ele])
c=0
i=1
while (1):
    if ('nineteen' in s):
        c = c+1
        s = s[7*i:]
        i = i+1
    else:
        break
    
print(max(min(l),c))


