h, w = map(int, input().split())
s = [input() for _ in range(h)]
dp = [[0]*w for _ in range(h)]
dp[0][0] = int(s[0][0] == '#')
for i in range(1, h): dp[i][0] = dp[i-1][0] + int(s[i-1][0]=='.' and s[i][0]=='#')
for j in range(1, w): dp[0][j] = dp[0][j-1] + int(s[0][j-1]=='.' and s[0][j]=='#')
for i in range(1, h):
    for j in range(1, w):
        up = dp[i-1][j] + int(s[i-1][j]=='.' and s[i][j]=='#')
        le = dp[i][j-1] + int(s[i][j-1]=='.' and s[i][j]=='#')
        dp[i][j] = min(up, le)
print(dp[-1][-1])