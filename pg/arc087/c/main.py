n = int(input())
a = list(map(int, input().split()))
d = {}
for ai in a:
    if ai not in d: d[ai] = 0
    d[ai] += 1
ans = 0
for di in d:
    nd = d[di]
    if nd >= di: ans += nd-di
    else: ans += nd
print(ans)