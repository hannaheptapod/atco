s, t = input(), input()

lens, lent = len(s), len(t)
s, t = 's'+s, 't'+t
dp = [[0]*(lent+1) for _ in range(lens+1)]

for i in range(1, lens+1):
    for j in range(1, lent+1):
        if s[i] == t[j]: dp[i][j] = dp[i-1][j-1]+1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ''
l = dp[-1][-1]
i, j = lens, lent

while l:
    if s[i] == t[j]:
        ans = s[i]+ans
        i, j, l = i-1, j-1, l-1
    elif dp[i][j] == dp[i-1][j]: i -= 1
    else: j -= 1

print(ans)