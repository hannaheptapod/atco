a, b = map(int, input().split())
ans = 4
if a+b >= 15 and b >= 8:
    ans = 1
elif a+b >= 10 and b >= 3:
    ans = 2
elif a+b >= 3:
    ans = 3
print(ans)