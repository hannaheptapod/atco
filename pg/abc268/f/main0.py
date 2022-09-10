from collections import Counter
import array

N = int(input())
S = [input() for _ in range(N)]
cnt = [[Counter(S[i])[j] for j in 'X123456789'] for i in range(N)]

arr = array.array('i')
for i in range(N):
    l, r, md = -1, i, 0
    while abs(l-r) > 1:
        md = (l+r)//2
        am = arr[md]

        s = cnt[am][0]*sum([cnt[i][j]*j for j in range(1, 10)])
        t = cnt[i][0]*sum([cnt[am][j]*j for j in range(1, 10)])
        if s > t: l = md
        else: r = md

    arr.insert(r, i)

ans = 0
for si in S:
    tmp = 0
    for sij in si:
        if sij == 'X': tmp += 1
        else: ans += tmp*int(sij)

cu = 0
for i in arr:
    for j in range(1, 10): ans += cu*cnt[i][j]*j
    cu += cnt[i][0]

print(ans)
