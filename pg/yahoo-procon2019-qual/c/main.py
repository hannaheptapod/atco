k, a, b = map(int, input().split())
if k < a or a+1 >= b: ans = k+1
else: ans = a + (b-a)*((k+1-a) // 2) + (k+1-a)%2
print(ans)