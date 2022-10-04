def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    G = [set() for _ in range(N)]
    for _ in range(M):  # 問題をよく読む（有向グラフ）
        x, y = map(lambda x: int(x)-1, input().split())
        G[x].add(y)

    ans = solve(N, A, G)
    print(ans)


def solve(N, A, G):
    dp = [float("inf")]*N

    for i in range(N):
        tmp = min(A[i], dp[i])
        for j in G[i]: dp[j] = min(dp[j], tmp)

    return max(A[i]-dp[i] for i in range(N))


if __name__ == '__main__': main()
