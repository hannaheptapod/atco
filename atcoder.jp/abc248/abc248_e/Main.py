from itertools import combinations

N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

if K == 1: ans = 'Infinity'
else:
    dic = {i: 0 for i in range(1, N+1)}
    for p1, p2 in combinations(P, 2):
        a, b = p2[1] - p1[1], -(p2[0] - p1[0])

        cnt = 0
        for xi, yi in P:
            if a*(xi-p1[0]) + b*(yi-p1[1]) == 0: cnt += 1

        dic[cnt] += 1

    ans = sum(2*dic[i]//(i*(i-1)) for i in range(K, N+1))

print(ans)
