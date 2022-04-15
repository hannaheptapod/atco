from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]

ans = 0
for A in combinations_with_replacement(range(1, M+1), N):
    tmp = 0
    for ai, bi, ci, di in query: tmp += di if A[bi-1] - A[ai-1] == ci else 0

    ans = max(ans, tmp)

print(ans)
