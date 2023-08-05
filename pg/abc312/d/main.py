def main():
    MOD = 998244353
    S = input()
    L = len(S)

    def solve():
        if L % 2 or S[0] == ')': return 0

        dp = [[0]*(L+1) for _ in range(L+1)]
        dp[0][0] = 1

        for i in range(L):
            for j in range(L):
                if S[i] != ')': 
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= MOD
                if j and S[i] != '(':
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= MOD
    
        return dp[L][0]
    
    ans = solve()
    print(ans)


if __name__ == '__main__': main()
