h, w = map(int, input().split())
a = [input() for _ in range(h)]
rows, cols = set(), set()
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            rows.add(i)
            cols.add(j)

for r in rows:
    s = str()
    for c in cols:
        s += a[r][c]
    print(s)