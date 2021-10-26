n, k = map(int, input().split())
a = list(map(int, input().split()))
l = r = 0
sm = a[0]
ans = 0
while r < n - 1 or sm >= k:
    if sm >= k:
        ans += n - r
        sm -= a[l]
        l += 1
    else:
        r += 1
        sm += a[r]
print(ans)