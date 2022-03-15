from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]

dist = [[-1] * W for _ in range(H)]
deq = deque([(i, j) for i in range(H) for j in range(W) if A[i][j] == '#'])
while deq:
    (i, j) = deq.popleft()
    if A[i][j] == '#': dist[i][j] = 0

    moves = []
    if i > 0: moves.append((i - 1, j))
    if i < H - 1: moves.append((i + 1, j))
    if j > 0: moves.append((i, j - 1))
    if j < W - 1: moves.append((i, j + 1))

    for (i_m, j_m) in moves:
        if dist[i_m][j_m] != -1: continue

        if A[i_m][j_m] == '#': dist[i_m][j_m] = 0
        else:
            dist[i_m][j_m] = dist[i][j] + 1
            deq.append((i_m, j_m))

ans = max([max(dij for dij in di) for di in dist])
print(ans)
