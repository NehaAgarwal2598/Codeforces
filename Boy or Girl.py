from collections import Counter
s = input()
c = len(Counter(s))
if c%2 == 0:
    print("CHAT WITH HER!")

else:
    print("IGNORE HIM!")
