N, K = map(int, input().split())
inv = int(str(K)[::-1])

ans = 0
if K <= inv:
    while K <= N:
        ans += 1
        K *= 10
    while inv <= N:
        ans += 1
        inv *= 10
if K == inv: ans //= 2
print(ans)
