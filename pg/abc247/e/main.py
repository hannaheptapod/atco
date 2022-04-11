N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

g = []
l, ix, iy = 0, set(), set()
for i in range(N):
    if A[i] == X: ix.add(i - l)
    if A[i] == Y: iy.add(i - l)
    if A[i] > X or A[i] < Y:
        g.append([i - l, ix, iy])
        l, ix, iy = i+1, set(), set()
if l < N: g.append([i - l + 1, ix, iy])

ans = 0
for leng, ix, iy in g:
    if not (ix and iy): continue

    cx, cy = 0, 0
    head, tail = 0, 0

    while head < leng:
        while tail < leng and not (cx and cy):
            if tail in ix: cx += 1
            if tail in iy: cy += 1
            tail += 1

        if cx and cy: ans += leng + 1 - tail

        if head in ix: cx -= 1
        if head in iy: cy -= 1
        head += 1

print(ans)
