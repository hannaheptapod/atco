n, m = map(int, input().split())
unu, di = set(), set()
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1 and b == n:
        ans = 'POSSIBLE'
        break
    if a == 1: unu.add(b)
    elif b == n: di.add(a)
else:
    for ui in unu:
        if ui in di:
            ans = 'POSSIBLE'
            break
    else: ans = 'IMPOSSIBLE'
print(ans)