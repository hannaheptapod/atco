from collections import deque

R, C = map(int, input().split())
S = tuple(map(int, input().split()))
G = tuple(map(int, input().split()))
MAZE = [input() for _ in range(R)]

dist = {(y, x):-1 for y, x in zip(range(R), range(C))}
dist[S] = 0

d = deque([S])
while d:
    y, x = d.popleft()

    move = []
    if y > 0: move.append((y-1, x))
    if y < R-1: move.append((y+1, x))
    if x > 0: move.append((y, x-1))
    if x < C-1: move.append((y, x+1))

    for v in move:
        if dist[v] != -1: continue

        dist[v] = dist[(y, x)] + 1
        d.append(v)

print(dist[G])