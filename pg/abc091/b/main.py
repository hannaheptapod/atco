n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ds = {}
for si in s:
    if si in ds: ds[si] += 1
    else: ds[si] = 1
for ti in t:
    if ti in ds: ds[ti] -= 1
ans = max(list(ds.values())+[0])
print(ans)