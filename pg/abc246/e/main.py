from collections import deque
import array
INF = 10**9

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = ['#'*(N+2)] + ['#' + input() + '#' for _ in range(N)] + ['#'*(N+2)]

dist = [[array.array('i', [INF]*(N+2)) for _ in range(N+2)] for _ in range(4)]
flag = [[array.array('b', [0]*(N+2)) for _ in range(N+2)] for _ in range(4)]
dx, dy = (1, 1, -1, -1), (1, -1, 1, -1)

nbr = [[i, A[0] + dx[i], A[1] + dy[i]] for i in range(4)]
deq = deque([[i, nx, ny] for i, nx, ny in nbr if S[nx][ny] == '.'])
for i, nx, ny in nbr: dist[i][nx][ny] = 1 if S[nx][ny] == '.' else INF

ans = -1
while deq:
    i, vx, vy = deq.popleft()
    if [vx, vy] == B:
        ans = dist[i][vx][vy]
        break

    if flag[i][vx][vy]: continue
    flag[i][vx][vy] = 1

    for j in range(4):
        wx, wy = vx + dx[j], vy + dy[j]
        if S[wx][wy] == '#': continue

        if i == j and dist[j][wx][wy] > dist[i][vx][vy]:
            deq.appendleft([j, wx, wy])
            dist[j][wx][wy] = dist[i][vx][vy]
        if i != j and dist[j][wx][wy] > dist[i][vx][vy] + 1:
            deq.append([j, wx, wy])
            dist[j][wx][wy] = dist[i][vx][vy] + 1

print(ans)
