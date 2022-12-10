def main():
    global N, K, D, A
    N, K, D = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)

    ans = knapsack()
    print(ans)


def knapsack():
    dp = [[[-1]*D for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 0

    for i, ai in enumerate(A):  # i番目までの整数から
        for j in range(N+1):  # j個選んで
            for k in range(D):  # S == k mod D となるような和Sの最大値
                x = dp[i][j][k]
                if x == -1: continue

                if x > dp[i+1][j][k]: dp[i+1][j][k] = x
                if x + ai > dp[i+1][j+1][(k+ai)%D]: dp[i+1][j+1][(k+ai)%D] = x + ai

    return dp[-1][K][0]


if __name__ == '__main__': main()
