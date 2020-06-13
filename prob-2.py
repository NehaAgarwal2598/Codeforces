q = int(input())
for _ in range(q):
    n, size = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    #l = []
    newseq = []
    splitsize = 1.0/size*n
    f= 0
    for i in range(size):
        newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])

    t = []
    for i in newseq:
        t.append(sum(i))
    f=0 
    for i in range(len(t)):
        if t[i]%2==0:
            print("NO")
            f=1
            break
        
    if f == 0:
        print("YES")

            
