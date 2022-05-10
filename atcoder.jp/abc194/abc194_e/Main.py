import array

N, M = map(int, input().split())
A = array.array('i', map(int, input().split()))

cnt = {i: 0 for i in range(N+1)}
for ai in A[:M]: cnt[ai] += 1
for i in range(N+1):
    if cnt[i]: continue

    ans = i
    break

for x in range(M, N):
    cnt[A[x]] += 1
    cnt[A[x-M]] -= 1

    if not cnt[A[x-M]]: ans = min(ans, A[x-M])

print(ans)
