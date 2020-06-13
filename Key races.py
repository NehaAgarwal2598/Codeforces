s, v1, v2, t1, t2 = list(map(int, input().split()))

x1 = v1*s+t1*2
x2 = v2*s+t2*2

if x1<x2:
    print("First")

elif x1>x2:
    print("Second")

else:
    print("Friendship")
