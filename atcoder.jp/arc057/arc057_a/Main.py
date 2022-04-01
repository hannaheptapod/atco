a, K = map(int, input().split())

if K:
    ans = 0
    while a < 2 * 10**12:
        a += a*K + 1
        ans += 1
else: ans = max(0, 2 * 10**12 - a)

print(ans)
