n = int(input())
ar = list(map(int, input().split()))
l = [0]*n
for i in range(n):
    l[ar[i]-1]= i+1

for i in l:
    print(i,end = ' ')
          
