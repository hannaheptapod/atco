n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
    if i >= k: ans += 1/n
    else:
        c = 2
        while i*c < k:
            c *= 2
        ans += 1/(c*n)
print(ans)