N, M, K = map(int, input().split())
p = []
for _ in range(M):
    p.append(list(map(int, input().split())))
w = [[1] + [0] * (N - 1)]

for day in range(K):
    ttl = sum(w[day])
    w.append([ttl - w[day][i] for i in range(N)])
    for pi in p:
        w[day + 1][pi[0]-1] -= w[day][pi[1]-1]
        w[day + 1][pi[1]-1] -= w[day][pi[0]-1]
print(w[K][0] % 998244353)