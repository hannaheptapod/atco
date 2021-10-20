t = int(input())
for _ in range(t):
    r, g, b = map(int, input().split())
    ans = 10**9
    if abs(g-b)%3 == 0: ans = min(ans, max(g, b))
    if abs(b-r)%3 == 0: ans = min(ans, max(b, r))
    if abs(r-g)%3 == 0: ans = min(ans, max(r, g))
    if ans < 10**9: print(ans)
    else: print(-1)