import array

N = int(input())
S = [input() for _ in range(N)]
cnt = [[0, 0] for _ in range(N)]
for i in range(N):
    for sij in S[i]:
        if sij == 'X': cnt[i][0] += 1
        else: cnt[i][1] += int(sij)

arr = array.array('i')
for i in range(N):
    l, r, md = -1, i, 0
    while abs(l-r) > 1:
        md = (l+r)//2
        am = arr[md]

        s = cnt[am][0]*cnt[i][1]
        t = cnt[i][0]*cnt[am][1]
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
    ans += cu*cnt[i][1]
    cu += cnt[i][0]

print(ans)
