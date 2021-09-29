n = int(input())
ver = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x not in ver:ver[x] = []
    ver[x] += [y]
for v in ver: ver[v].sort()
vn = len(ver)
vl = list(ver)
ans = 0
for i in range(vn - 1):
    x1 = vl[i]
    v1 = ver[x1]
    m = len(v1)
    for j in range(i + 1, vn):
        x2 = vl[j]
        v2 = ver[x2]
        n = len(v2)
        y1 = y2 = 0
        com = 0
        while y1 < m and y2 < n:
            if v1[y1] == v2[y2]: com += 1
            if v1[y1] <= v2[y2]: y1 += 1
            else: y2 += 1
        ans += com * (com - 1) // 2

print(ans)