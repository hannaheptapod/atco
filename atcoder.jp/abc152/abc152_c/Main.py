n = int(input())
p = list(map(int, input().split()))
mn = p[0]
ans = 0
for pi in p:
    if pi <= mn: ans += 1
    mn = min(mn, pi)
print(ans)