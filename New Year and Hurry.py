n, k = list(map(int, input().split()))
time = 240
diff = time-k
t=0
prob = 0
for i in range(1,n+1):
    if (t+5*i)<=diff:
        t = t+5*i
        prob +=1

print(prob)

    
    
