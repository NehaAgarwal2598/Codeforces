t = int(input())
for _ in range(t):
    a, b, k = list(map(int, input().split()))
    xb = k//2
    xa = k-xb
    x = xa*a-xb*b

    print(x)
