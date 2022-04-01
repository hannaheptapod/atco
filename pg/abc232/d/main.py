H, W = map(int, input().split())
C = ['#'*(W+2)] + ['#'+input()+'#' for _ in range(H)] + ['#'*(W+2)]

dp = [[int(C[i][j] == '.') for j in range(W+2)] for i in range(H+2)]

for i in range(H, 0, -1):
    for j in range(W, 0, -1):
        if C[i][j] == '#': continue
        dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + 1

ans = dp[1][1]
print(ans)
