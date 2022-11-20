def main():
    global INF, N, A
    INF = 10**18
    N = int(input())
    A = tuple(map(int, input().split()))

    ans = solve()
    print(ans)


def solve():
    dp = [[[0, 0], [0, 0]] for _ in range(N)]
    dp[0] = [[0, INF], [INF, A[0]]]

    for i in range(1, N): dp[i] = [[dp[i-1][j][1], min(dp[i-1][j]) + A[i]] for j in range(2)]

    return min(dp[-1][0][1], min(dp[-1][1]))


if __name__ == '__main__': main()
