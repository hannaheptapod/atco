x, y = map(int, input().split('.'))
if y <= 2: ans = str(x)+'-'
elif y <= 6: ans = str(x)
else: ans = str(x)+'+'
print(ans)