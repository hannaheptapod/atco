def main():
    global N, M, pos
    N, M = map(int, input().split())
    pos = [tuple(map(int, input().split())) for _ in range(N+M)]

    ans = f'{tsp():.10f}'
    print(ans)


def tsp():
    dp = [[float('inf') for _ in range(1<<(N+M))] for _ in range(N+M+1)]
    for i in range(N+M): dp[i][1<<i] = dist(pos[i], (0, 0))

    for s in range(1, 1<<(N+M)):
        coef = 0.5**popcount[s>>N]

        for i in range(N+M):
            if not s>>i & 1: continue

            for j in range(N+M):
                if s>>j & 1: continue

                tmp = dp[i][s] + coef * dist(pos[i], pos[j])
                if tmp < dp[j][s^(1<<j)]: dp[j][s^(1<<j)] = tmp

    ret = float('inf')
    for i in range(N+M):
        for s in range((1<<N)-1, 1<<(N+M), 1<<N):
            coef = 0.5**popcount[s>>N]
            tmp = dp[i][s] + coef * dist(pos[i], (0, 0))
            if tmp < ret: ret = tmp

    return ret


popcount = [0]*(1<<5)
for i in range(1, 1<<5): popcount[i] = popcount[i>>1] + (i&1)


def dist(u, v): return ((u[0]-v[0])**2 + (u[1]-v[1])**2)**0.5


if __name__ == '__main__': main()
