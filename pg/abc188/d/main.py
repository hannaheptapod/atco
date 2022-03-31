N, C = map(int, input().split())
diff = {}
for _ in range(N):
    a, b, c = map(int, input().split())

    if a-1 not in diff: diff[a-1] = 0
    diff[a-1] += c
    if b not in diff: diff[b] = 0
    diff[b] -= c

diff = sorted(diff.items())

ans = 0
now, sm = 0, 0
for dt, df in diff:
    ans += (dt-now)*min(sm, C)
    now = dt
    sm += df

print(ans)
