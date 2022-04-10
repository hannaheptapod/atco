N, x = map(int, input().split())
a = [0] + list(map(int, input().split()))

ans = 0
for i in range(1, N+1):
    e = max(0, a[i-1]+a[i] - x)
    ans += e
    a[i] -= e

print(ans)
