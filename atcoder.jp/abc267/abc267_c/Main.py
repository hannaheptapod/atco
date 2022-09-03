N, M = map(int, input().split())
A = list(map(int, input().split()))

sm = sum(A[:M])
now = sum([(i+1)*A[i] for i in range(M)])
ans = now

for i in range(N-M):
    now += M*A[i+M] - sm
    ans = max(ans, now)
    sm += A[i+M] - A[i]

print(ans)
