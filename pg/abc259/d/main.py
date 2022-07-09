from collections import deque

N = int(input())
sx, sy, tx, ty = map(int, input().split())
cir = [list(map(int, input().split())) for _ in range(N)]

graph = {i: set() for i in range(N+2)}

for i in range(N):
    for j in range(i, N):
        if i == j: continue

        d = (cir[i][0]-cir[j][0])**2 + (cir[i][1]-cir[j][1])**2
        if d >= (cir[i][2]-cir[j][2])**2 and d <= (cir[i][2]+cir[j][2])**2:
            graph[i].add(j)
            graph[j].add(i)

    if (cir[i][0]-sx)**2 + (cir[i][1]-sy)**2 == cir[i][2]**2: graph[N].add(i)
    if (cir[i][0]-tx)**2 + (cir[i][1]-ty)**2 == cir[i][2]**2: graph[i].add(N+1)

seen = [0]*(N+2)
deq = deque([N])
while deq:
    now = deq.popleft()
    if seen[now]: continue
    seen[now] = 1

    for nxt in graph[now]:
        if not seen[nxt]: deq.append(nxt)

ans = 'Yes' if seen[-1] else 'No'
print(ans)
