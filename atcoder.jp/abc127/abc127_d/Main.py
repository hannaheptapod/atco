n, m = map(int, input().split())
a = list(map(int, input().split()))
c = [[0, n]]
for _ in range(m):
    bi, ci = map(int, input().split())
    c.append([ci, bi])
a.sort(reverse=True)
c.sort(reverse=True)
cnt = 0
na = nc = 0
ans = 0
while cnt < n:
    ai, ci = a[na], c[nc]
    if ai > ci[0]:
        ans += ai
        cnt += 1
        na += 1
    else:
        ans += ci[0]*min(ci[1], n - cnt)
        cnt += ci[1]
        nc += 1
print(ans)