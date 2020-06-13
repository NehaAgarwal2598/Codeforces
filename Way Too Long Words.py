n = int(input())
for _ in range(n):
    e = input()
    if len(e) >10:
        print(e[0]+str(len(e)-2)+e[len(e)-1])
    else:
        print(e)
