x, y = map(int, input().split())
if -x == y: ans = 1
elif x*y < 0: ans = abs(x + y) + 1
elif x*y == 0: ans = abs(x + y) + int(x > y)
elif x < y: ans = y - x
else: ans = x - y + 2
print(ans)