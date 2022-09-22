def main():
    global N, P, C
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    C = [[cost(i, j) for j in range(N)] for i in range(N)]

    ans = solve()
    print(ans)


def cost(x, y): return abs(P[x][0]-P[y][0]) + abs(P[x][1]-P[y][1]) + max(0, P[y][2]-P[x][2])


def solve():  # 巡回セールスマン => bitDP
    dp = [[float('inf')]*N for _ in range(1<<N)]
    dp[0][0] = 0

    for s in range(1<<N):
        for v in range(N):
            for u in range(N):
                if not s>>u & 1 and s: continue

                if not s>>v & 1 and dp[s][u] + C[u][v] < dp[s | 1<<v][v]:
                    dp[s | 1<<v][v] = dp[s][u] + C[u][v]

    ret = dp[-1][0]
    return ret if ret != float('inf') else -1


if __name__ == '__main__': main()
