N, L, R = map(int, input().split())
A = list(map(int, input().split()))

f, g = [[0]*(N+1) for _ in range(2)]
for i in range(N):
    f[i+1] = min(f[i]+A[i], L*(i+1))
    g[i+1] = min(g[i]+A[N-i-1], R*(i+1))

ans = sum(A)
for i in range(N+1): ans = min(ans, f[i] + g[N-i])

print(ans)
