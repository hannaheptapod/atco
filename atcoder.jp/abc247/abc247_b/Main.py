N = int(input())
st = [list(input().split()) for _ in range(N)]
cnt = {}
for s, t in st:
    if s not in cnt: cnt[s] = 0
    if t not in cnt: cnt[t] = 0
    cnt[s] += 1
    cnt[t] += 1
    if s == t: cnt[s] -= 1

for s, t in st:
    if cnt[s] == 1 or cnt[t] == 1: continue
    else:
        ans = 'No'
        break
else: ans = 'Yes'

print(ans)
