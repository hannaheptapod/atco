n, a, b = map(int, input().split())
if abs(a - b)%2 == 0: ans = abs(a - b)//2
else: ans = min(-int(-(a + b)//2)-1, -int(-(2*n - a - b)//2))
print(ans)