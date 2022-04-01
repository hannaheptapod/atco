N = int(input())
A = [0] + list(map(int, input().split()))

p, q = [0]*(N+1), [0]*(N+1)
for i in range(1, N+1):
    p[i] = p[i-1] + A[i]
    q[i] = max(q[i-1], p[i])

ans = 0
now = 0
for i in range(1, N+1):
    ans = max(ans, now + q[i])
    now += p[i]

print(ans)
