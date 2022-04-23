from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

comp = sorted(set(A))
mx = comp[-1]

ans = 0
for i in range(len(comp)):
    ai = comp[i]

    for j in range(i, len(comp)):
        aj = comp[j]

        if ai*aj > mx: break
        ak = ai*aj

        if ak not in cnt: continue

        ans += 2*cnt[ai]*cnt[aj]*cnt[ak] if ai != aj else cnt[ai]*cnt[aj]*cnt[ak]

print(ans)
