n, k = list(map(int, input().split()))

no_red = 2*n
no_green = 5*n
no_blue = 8*n

req_red = no_red//k
req_green = no_green//k
req_blue = no_blue//k

if no_red%k !=0:
    req_red +=1


if no_green%k !=0:
    req_green +=1

if no_blue%k != 0:
    req_blue +=1

print(req_red+req_green+req_blue)
