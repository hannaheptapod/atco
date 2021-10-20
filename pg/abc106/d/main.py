N, M, Q = map(int, input().split())
tran = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    L, R = map(int, input().split())
    tran[L][R] += 1
for l in range(1, N+1):
    for r in range(1, N+1):
        tran[l][r] += tran[l][r-1]
for _ in range(Q):
    p, q = map(int, input().split())
    ans = 0
    for l in range(p, q+1):
        ans += tran[l][q]
    print(ans)