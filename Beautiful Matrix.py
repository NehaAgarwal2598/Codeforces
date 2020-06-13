a = []
for _ in range(5):
    a.append(list(map(int, input().split())))

f=0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            r = i
            c = j
            f=1
            break

    if f==1 :
        break

print(abs(2-r)+abs(2-c))
