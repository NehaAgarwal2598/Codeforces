n, c = list(map(int, input().split()))
p = list(map(int, input().split()))
t = list(map(int, input().split()))
limak = 0
Radewoosh = 0
sm, sm2 =0,0
for i in range(n):
    sm +=t[i]
    sm2 +=t[n-i-1]
    limak += max(0,p[i] - c*sm)
    Radewoosh += max(0,p[n-i-1] - c*sm2)

if limak > Radewoosh:
    print("Limak")

elif limak < Radewoosh:
    print("Radewoosh")

else:
    print("Tie")
