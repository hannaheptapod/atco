from bisect import bisect_right as br

N, T = map(int, input().split())
AB = [[]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N + 1):
    dp[i][0] = dp[i-1][0] + AB[i][0]
    
    for j in range(1, i + 1): dp[i][j] = min(dp[i-1][j]+AB[i][0], dp[i-1][j-1]+AB[i][1])

ng, ok = -1, N+1
while ng+1 < ok:
    md = (ng + ok)//2
    
    if dp[-1][md] <= T: ok = md
    else: ng = md

if ok <= N: ans = ok
else: ans = -1
print(ans)
