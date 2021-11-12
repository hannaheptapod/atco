w, h, n = map(int, input().split())
l, r, b, t = 0, w, 0, h
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1: l = max(l, x)
    elif a == 2: r = min(r, x)
    elif a == 3: b = max(b, y)
    else: t = min(t, y)
ans = max(0, r-l)*max(0, t-b)
print(ans)