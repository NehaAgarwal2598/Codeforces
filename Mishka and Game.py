n = int(input())
mis, chris = 0, 0
for _ in range(n):
    m, c = list(map(int, input().split()))
    if m > c:
        mis +=1
    elif c > m:
        chris +=1


if mis > chris :
    print("Mishka")

elif chris > mis:
    print("Chris")

else:
    print("Friendship is magic!^^")
