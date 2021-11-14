n = int(input())
alp = {ai:50 for ai in 'abcdefghijklmnopqrstuvwxyz'}
for _ in range(n):
    s = input()
    d = {}
    for si in s:
        if si not in d: d[si] = 0
        d[si] += 1
    for ai in alp:
        if ai in d: alp[ai] = min(alp[ai], d[ai])
        else: alp[ai] = 0
ans = ''
for ai in alp: ans += ai*alp[ai]
print(ans)