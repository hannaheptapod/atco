from bisect import bisect
from itertools import permutations
n, s = int(input()), input()
alp = {'A': 0, 'B': 1, 'C': 2}
id = [[] for _ in range(3)]
for i in range(3*n): id[alp[s[i]]].append(i)
ans = ['x']*(3 * n)
cnt = n
for num in range(1, 6+1):
    for pi in permutations([0, 1, 2]):
        if id[pi[0]][0] < id[pi[1]][0] and id[pi[0]][0] < id[pi[2]][0] and id[pi[1]][-1] < id[pi[2]][-1]:
            o1, o2, o3 = pi
            break
    ok = 0
    ng = cnt+1
    while abs(ok - ng) > 1:
        md = (ok + ng) // 2
        left, right = id[o1][md-1], id[o3][cnt-md]
        l, r = bisect(id[o2], left), bisect(id[o2], right)
        if r-l < md: ng = md
        else: ok = md
    din = bisect(id[o2], id[o1][ok-1])
    for i in (id[o1][:ok]+id[o2][din:din+ok]+id[o3][cnt-ok:]):
        ans[i] = str(num)
    id[o1], id[o2], id[o3] = id[o1][ok:], id[o2][:din]+id[o2][din+ok:], id[o3][:cnt-ok]
    cnt -= ok
    if cnt: continue
    break
print(''.join(ans))