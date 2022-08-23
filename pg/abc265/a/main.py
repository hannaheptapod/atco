X, Y, N = map(int, input().split())

if X*3 <= Y: ans = X*N
else: ans = X*(N%3) + Y*(N//3)

print(ans)
