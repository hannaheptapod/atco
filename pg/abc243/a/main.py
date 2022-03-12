V, A, B, C = map(int, input().split())
sm = A + B + C

if V%sm < A: ans = 'F'
elif V%sm < A+B: ans = 'M'
else: ans = 'T'

print(ans)
