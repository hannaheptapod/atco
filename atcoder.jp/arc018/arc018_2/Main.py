from itertools import combinations

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b, c in combinations(xy, 3):
    s = abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]))
    if s and not s%2: ans += 1

print(ans)
