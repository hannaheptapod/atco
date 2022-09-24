def main():
    N, _ = map(int, input().split())
    A = list(map(int, input().split()))

    ans = solve(N, A)
    print(ans)


def solve(n, a):
    dp = [0]*(n+1)

    for i in range(1, n+1):
        for aj in a:
            if aj > i: break
            dp[i] = max(dp[i], i-dp[i-aj])

    return dp[n]


if __name__ == '__main__': main()
