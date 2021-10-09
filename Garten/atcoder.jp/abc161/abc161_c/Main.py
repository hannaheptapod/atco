n, k = map(int, input().split())
n %= k
ans = min(n, abs(n - k))
print(ans)