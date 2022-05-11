from bisect import bisect_right as bir

N, K = map(int, input().split())
A = list(map(int, input().split()))

cs = 0
dic, inv = {}, {}

for i in range(N):
    cs += A[i]

    dic[i] = cs
    if cs not in inv: inv[cs] = []
    inv[cs].append(i)

ans = 0
for i in range(N):
    l = dic[i]
    if l == K: ans += 1
    r = l + K

    if r not in inv: continue

    ans += len(inv[r]) - bir(inv[r], i)

print(ans)
