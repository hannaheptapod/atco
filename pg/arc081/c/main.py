n = int(input())
a = list(map(int, input().split()))
d = {}
di, kvar = set(), set()
for ai in a:
    if ai not in d: d[ai] = 1
    else:
        d[ai] += 1
        if d[ai] == 2: di.add(ai)
        if d[ai] == 4: kvar.add(ai)
ldi, lkvar = sorted(di, reverse=True), sorted(kvar, reverse=True)
if len(ldi) >= 2: ans = ldi[0]*ldi[1]
else: ans = 0
if len(lkvar) > 0: ans = max(ans, lkvar[0]**2)
print(ans)