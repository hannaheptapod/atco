from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = [set() for _ in range(N + 1)]
for abi in AB:
    a, b = abi
    G[a].add(b)
    G[b].add(a)

ans = 1
seen = [True] + [False]*N

for i in range(1, N + 1):
    if seen[i]: continue
    
    d = deque([i])
    tmp = 1
    while d:
        now = d.popleft()
        seen[now] = True
        
        for move in G[now]:
            if seen[move]: continue
            
            seen[move] = True
            d.append(move)
            tmp += 1

    ans = max(ans, tmp)

print(ans)
