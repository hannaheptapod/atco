N = int(input())
S = [input() for _ in range(N)]

ans = 10**3
for x in map(str, range(10)):
    cnt = [0]*10
    for i in range(N): cnt[S[i].index(x)] += 1

    mx = max(cnt)
    for i in range(10):
        if cnt[i] == mx: mod = i

    ans = min(ans, 10*(mx-1) + mod)

print(ans)
