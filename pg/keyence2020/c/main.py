n, k, s = map(int, input().split())
ans = [s]*k
if s < 10**9: ans += [s+1]*(n-k)
else: ans += [s-1]*(n-k)
print(*ans)