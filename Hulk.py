n = int(input())
emotion = ["hate", "love"]
if n == 1:
    print("I "+emotion[0]+" it")
else:
    for i in range(1,n+1):
        print("I", end = ' ')
        if i%2 == 0:
            print(emotion[1], end=' ')
        else:
            print(emotion[0], end = ' ')
        if i<n:
            print("that", end=' ')

    print("it")
