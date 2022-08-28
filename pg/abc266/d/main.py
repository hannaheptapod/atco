N = int(input())

TXA = [list(map(int, input().split())) for _ in range(N)]
dic = {Ti: [Xi, Ai] for Ti, Xi, Ai in TXA}

T_max = TXA[-1][0]
dp = [0]*5

for i in range(1, T_max+1):
    prev = dp.copy()

    for j in range(min(i+1, 5)):
        dp[j] = max([prev[max(j-1, 0)], prev[j], prev[min(j+1, 4)]])

        if i in dic and dic[i][0] == j: dp[j] += dic[i][1]

ans = max(dp)
print(ans)
