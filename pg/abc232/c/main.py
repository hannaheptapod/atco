from itertools import permutations

N, M = map(int, input().split())
tak = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    tak[a][b] = tak[b][a] = 1
aok = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    aok[a][b] = aok[b][a] = 1

for p in permutations(range(N), N):
    id = {i: p[i] for i in range(N)}

    for i in range(N):
        for j in range(N):
            if tak[i][j] != aok[id[i]][id[j]]: break
        else: continue
        break
    else:
        ans = 'Yes'
        break
else: ans = 'No'

print(ans)
