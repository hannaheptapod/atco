MOD = 998244353


def main():
    N, K = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(K)]

    ans = solve(N, S)
    print(ans)


def solve(n, s):
    dp = [0]*n
    dp[0], dp[1] = 1, -1

    for i in range(n):
        if i: dp[i] += dp[i-1]
        dp[i] %= MOD

        for l, r in s:
            if i+l < n:
                dp[i+l] += dp[i]
                dp[i+l] %= MOD
            if i+r+1 < n:
                dp[i+r+1] -= dp[i]
                dp[i+r+1] %= MOD

    return dp[-1]


if __name__ == '__main__': main()
