from bisect import insort_left, bisect_left
n, m = map(int, input().split())

py = [list(map(int, input().split())) for _ in range(m)]

d = {}
for pyi in py:
    p, y = pyi

    if p not in d: d[p] = [0]
    insort_left(d[p], y)

for pyi in py:
    p, y = pyi

    ans = str(p).zfill(6) + str(bisect_left(d[p], y)).zfill(6)

    print(ans)