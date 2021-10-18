n, t = map(int, input().split())
tl = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    ans += min(t, tl[i+1] - tl[i])
ans += t
print(ans)