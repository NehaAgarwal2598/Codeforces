n = int(input())
step = [1, 2, 3, 4, 5]
c = 0
while n!=0:
    mx = 0
    for i in step:
        if i>mx and  mx< n:
            mx = i
            d = n//mx

    n = n-(d*mx)
    c = c+d

print(c)
