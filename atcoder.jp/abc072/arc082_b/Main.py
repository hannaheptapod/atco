n = int(input())
p = list(map(int, input().split()))
l = p[0]
ans = 0
for i in range(1, n):
    r = p[i]
    if l == i: ans += 1
    else: l = r
if l == n: ans += 1
print(ans)