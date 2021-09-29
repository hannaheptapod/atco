a, b = map(int, input().split())
ans = b - a + 1
if a > b:
    ans = 0
print(ans)