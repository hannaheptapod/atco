N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = {}
for ai in A:
    if ai not in cnt: cnt[ai] = 1
    else: cnt[ai] += 1
for bi in B:
    if bi not in cnt:
        ans = 'No'
        break
    else: cnt[bi] -= 1
    if cnt[bi] < 0:
        ans = 'No'
        break
else: ans = 'Yes'

print(ans)