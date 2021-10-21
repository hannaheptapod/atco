a, b, c, k = map(int, input().split())
ans = (a - b) * (-1)**k
if abs(ans) > 10**18: ans = 'Unfair'
print(ans)