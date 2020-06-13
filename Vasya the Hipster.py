a, b = list(map(int, input().split()))
diff = min(a,b)
mx = max(a,b)
same = (mx-diff)//2
print(diff, same)
