gems = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']
color = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']

n = int(input())
l =[]
for _ in range(n):
    l.append(input())

print(6-n)
for i in color:
    if i not in l:
        print(gems[color.index(i)])
