t = int(input())
for _ in range(t):
    a, b, n = list(map(int, input().split()))
    n = n%3
    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        print(a^b)
