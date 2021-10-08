n, k = map(int, input().split())
a = list(map(int, input().split()))

d = n - a[-1] + a[0]
for i in range(k - 1): d = max(d, a[i+1] - a[i])
ans = n - d
print(ans)