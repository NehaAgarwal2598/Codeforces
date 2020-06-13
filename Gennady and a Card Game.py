s = input()
#rank = {'2','3','4','5','6','7','8','9','T','J','Q','K','A'}
#suit = {'D','C','S','H'}
a = list(input().split())
f=1
for i in a:
    if s[0:1] == i[0:1] or s[1:] == i[1:]:
        print("YES")
        f = 0
        break

if f==1:
    print("NO")
