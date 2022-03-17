N = int(input())
f = list(map(lambda x: int(x)-1, input().split()))
MOD = 998244353

ans = 1
seen = [False]*N

for i in range(N):
    if seen[i]: continue

    visited = set()
    now = i

    while not seen[now]:
        seen[now] = True
        visited.add(now)
        now = f[now]

    if now in visited:
        ans *= 2
        ans %= MOD

ans -= 1
print(ans)
