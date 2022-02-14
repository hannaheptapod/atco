from bisect import bisect_right

N, W = map(int, input().split())
item = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

INF = 10**10
sm = sum([it[1] for it in item])
dp = [[0]*sm+[INF]*sm for _ in range(N+1)]

for i in range(1, N+1):
    w, v = item[i]
    
    for j in range(sm, 2*sm): dp[i][j] = min(dp[i-1][j], dp[i-1][j-v]+w)

bottom = dp[-1]

ans = bisect_right(bottom, W) - sm

print(ans)