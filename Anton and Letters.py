n = list(input().split(', '))

if n[0] == '{}':
    print('0')

else:
    n[0]= n[0][1:]
    n[len(n)-1] = n[len(n)-1][0:1]
    print(len(list(set(n))))
    
