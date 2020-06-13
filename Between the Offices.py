n = int(input())
s = list(input())
fran = 0
sea = 0
for i in range(n-1):
    if s[i]== 'F' and s[i+1] == 'S':
        fran +=1
    elif s[i]== 'S' and s[i+1] == 'F':
        sea +=1


if sea > fran :
    print("Yes")

else:
    print("No")
