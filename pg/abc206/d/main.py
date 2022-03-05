N = int(input())
A = list(map(int, input().split()))

G = []
d = {}
id = 0
for i in range(N):
    if A[i] not in d:
        G.append([])
        d[A[i]] = id
        id += 1
    G[d[A[i]]].append(i)

print(G)
