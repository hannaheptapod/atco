a, b = map(int, input().split())

if (a == 1 and b == 10) or (a < 10 and b-a == 1) or (a == 10 and b == 1): ans = 'Yes'
else: ans = 'No'

print(ans)