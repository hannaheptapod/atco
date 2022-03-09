from collections import deque

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    c, d = map(lambda x: int(x)-1, input().split())
    G[c].append(d)
    G[d].append(c)

seen = [False]*N
d = deque()
for i in range(N):
    if seen[i]: continue
    
    a_sum, b_sum = 0, 0
    d.append(i)
    while d:
        now = d.popleft()
        if not seen[now]:
            seen[now] = True
            a_sum += a[now]
            b_sum += b[now]
            
        for move in G[now]:
            if seen[move]: continue
            
            seen[move] = True
            a_sum += a[move]
            b_sum += b[move]
            d.append(move)
    
    if a_sum == b_sum: continue
    ans = 'No'
    break
else: ans = 'Yes'

print(ans)
