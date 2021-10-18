r, g, b, n = map(int, input().split())
ans = 0
for i in range(0, n+1, r):
    for j in range(0, n+1, g):
        if n-i-j >= 0 and not (n-i-j) % b: ans += 1
print(ans)