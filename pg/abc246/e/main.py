from collections import deque
import array
INF = 10**9

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = ['#'*(N+2)] + ['#' + input() + '#' for _ in range(N)] + ['#'*(N+2)]

dist = array.array('i', [INF]*((N+2)**2 * 4))
flag = array.array('b', [0]*((N+2)**2 * 4))
dx, dy = (1, 1, -1, -1), (1, -1, 1, -1)


def id(x, y, i): return x*(N+2)*4 + y*4 + i


nbr = [[A[0] + dx[i], A[1] + dy[i], i] for i in range(4)]
deq = deque([[nx, ny, i] for nx, ny, i in nbr if S[nx][ny] == '.'])
for nx, ny, i in nbr: dist[id(nx, ny, i)] = 1 if S[nx][ny] == '.' else INF

ans = -1
while deq:
    vx, vy, i = deq.popleft()
    if [vx, vy] == B:
        ans = dist[id(vx, vy, i)]
        break

    if flag[id(vx, vy, i)]: continue
    flag[id(vx, vy, i)] = 1

    for j in range(4):
        wx, wy = vx + dx[j], vy + dy[j]
        if S[wx][wy] == '#': continue

        di = dist[id(vx, vy, i)]
        if i == j and dist[id(wx, wy, j)] > di:
            deq.appendleft([wx, wy, j])
            dist[id(wx, wy, j)] = di
        if i != j and dist[id(wx, wy, j)] > di + 1:
            deq.append([wx, wy, j])
            dist[id(wx, wy, j)] = di + 1

print(ans)
