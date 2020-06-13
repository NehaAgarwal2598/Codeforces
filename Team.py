n = int(input())
sm = 0
for _ in range(n):
    a = list(map(int, input().split()))
    if sum(a) >= 2:
        sm +=1
print(sm)
