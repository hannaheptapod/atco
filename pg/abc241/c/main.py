N = int(input())
S = [input() for _ in range(N)]

dp = [[[0]*8 for _ in range(N+10)] for _ in range(N+10)]

for i in range(5, N+5):
    for j in range(5, N+5):
        sij = int(S[i-5][j-5] == '#')

        for d in range(6):
            dp[i][j+d][0] += sij
            dp[i][j-d][1] += sij
            dp[i+d][j][2] += sij
            dp[i-d][j][3] += sij
            dp[i+d][j+d][4] += sij
            dp[i+d][j-d][5] += sij
            dp[i-d][j+d][6] += sij
            dp[i-d][j-d][7] += sij

for i in range(5, N+5):
    for j in range(5, N+5):
        dpij = dp[i][j]
        tmp = 0

        if j < N: tmp = max(tmp, dpij[1])
        if j >= 10: tmp = max(tmp, dpij[0])
        if i < N: tmp = max(tmp, dpij[3])
        if i >= 10: tmp = max(tmp, dpij[2])
        if j < N and i < N: tmp = max(tmp, dpij[7])
        if j >= 10 and i < N: tmp = max(tmp, dpij[6])
        if j < N and i >= 10: tmp = max(tmp, dpij[5])
        if j >= 10 and i >= 10: tmp = max(tmp, dpij[4])

        if tmp >= 4:
            ans = 'Yes'
            break
    else: continue
    break
else: ans = 'No'

print(ans)