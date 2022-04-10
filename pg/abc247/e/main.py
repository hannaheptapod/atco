

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

g = []
l, ix, iy = 0, [], []
for i in range(N):
    if A[i] == X: ix.append(i - l)
    if A[i] == Y: iy.append(i - l)
    if A[i] > X or A[i] < Y:
        g.append([i - l + 1, ix, iy])
        l, ix, iy = i+1, [], []
if l < N: g.append([i - l + 1, ix, iy])

ans = 0
