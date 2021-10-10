n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
sm = 0
ans = 0
for ai in a:
    sm += ai
    if sm > x: break
    elif sm == x:
        ans += 1
        break
    elif ans < n - 1: ans += 1
print(ans)