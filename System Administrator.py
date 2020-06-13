n = int(input())
x1, y1, x2, y2 = 0, 0, 0, 0
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        x1 = x1+a[1]
        y1 = y1+a[2]

    else:
        x2 = x2+a[1]
        y2 = y2+a[2]

if x1>=y1:
    print("LIVE")
else:
    print("DEAD")
    
if x2>=y2:
    print("LIVE")
else:
    print("DEAD")
