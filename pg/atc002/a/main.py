from collections import deque

R, C = map(int, input().split())
S = tuple(map(lambda x: int(x)-1, input().split()))
G = tuple(map(lambda x: int(x)-1, input().split()))
MAZE = [input() for _ in range(R)]

dist = {(y, x):-1 for y in range(R) for x in range(C)}
dist[S] = 0

d = deque([S])
while d:
    y, x = d.popleft()

    move = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

    for v in move:
        if MAZE[v[0]][v[1]] == '#' or dist[v] != -1: continue

        dist[v] = dist[(y, x)] + 1
        d.append(v)

print(dist[G])