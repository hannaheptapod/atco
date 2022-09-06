N, Q = map(int, input().split())
a = list(map(int, input().split()))
cnt = {}
for i in range(N):
    if a[i] not in cnt: cnt[a[i]] = []
    cnt[a[i]].append(i+1)

for _ in range(Q):
    x, k = map(int, input().split())
    if x not in cnt or k > len(cnt[x]): print(-1)
    else: print(cnt[x][k-1])
