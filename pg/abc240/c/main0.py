N, X = map(int, input().split())
jump = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[1]+[0]*X] + [[0]*(X+1) for _ in range(N)]

for i in range(1, N+1):
    ai, bi = jump[i]
    for j in range(X-ai+1):
        if dp[i-1][j] == 1:
            dp[i][j+ai] = 1
            if j+bi <= X: dp[i][j+bi] = 1

if dp[N][X]: ans = 'Yes'
else: ans = 'No'

print(ans)