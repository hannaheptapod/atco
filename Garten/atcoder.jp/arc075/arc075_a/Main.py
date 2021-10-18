n = int(input())
s = [int(input()) for _ in range(n)]
sm = sum(s)
dp = [[False]*(sm + 1) for _ in range(n+1)]
dp[0][0] = True
for i in range(1, n+1):
    for j in range(sm + 1):
        if dp[i-1][j]: dp[i][j] = dp[i][j + s[i-1]] = True
for j in range(sm, -1, -1):
    if j%10:
        for i in range(n+1):
            if dp[i][j]:
                print(j)
                break
        else: continue
        break
    elif j == 0: print(0)