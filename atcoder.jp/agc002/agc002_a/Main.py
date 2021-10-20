a, b = map(int, input().split())
if a > 0: ans = 'Positive'
elif a == 0: ans = 'Zero'
elif b >= 0: ans = 'Zero'
elif (a - b) % 2: ans = 'Positive'
else: ans = 'Negative'
print(ans)