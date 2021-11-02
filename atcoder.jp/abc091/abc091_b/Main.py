n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ds, dt = {}, {}
for si in s:
    if si in ds: ds[si] += 1
    else: ds[si] = 1
for ti in t:
    if ti in dt: dt[ti] += 1
    else: dt[ti] = 1
ans = 0
for si in ds:
    if si in dt: p = ds[si] - dt[si]
    else: p = ds[si]
    ans = max(ans, p)
print(ans)