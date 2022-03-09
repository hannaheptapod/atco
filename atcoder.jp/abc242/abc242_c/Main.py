N = int(input())
MOD = 998244353

dp = [0] + [1]*9

for _ in range(1, N):
    next = [0]*10
    
    for i in range(1, 10):
        next[i] = dp[i]
        
        if i > 1: next[i] += dp[i-1]
        if i < 9: next[i] += dp[i+1]

    dp = [n%MOD for n in next]

ans = sum(dp) % MOD
print(ans)
