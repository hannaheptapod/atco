INF = 10**18


def main():
    global N, G, E
    N, M, _ = map(int, input().split())
    G = [_ for _ in range(M)]
    for i in range(M):
        a, b, c = map(int, input().split())
        G[i] = [a-1, b-1, c]
    E = list(map(lambda x: int(x)-1, input().split()))

    ans = solve()
    print(ans)


def solve():
    dp = [0] + [INF]*(N-1)

    for e in E:
        a, b, c = G[e]
        cost = dp[a] + c
        if b and cost < dp[b]: dp[b] = cost

    ret = dp[N-1]
    return ret if ret < INF else -1


if __name__ == '__main__': main()
