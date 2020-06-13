n = int(input())
s = input()
an, da = 0, 0

for i in s:
    if i=='A':
        an +=1

    else:
        da +=1

if an>da:
    print("Anton")

elif da>an:
    print("Danik")
else:
    print("Friendship")
