h, w = map(int, input().split())
a = [input() for _ in range(h)]
sm = 0
for i in range(h):
    for j in range(w): sm += int(a[i][j] == '#')
if sm == h+w-1: ans = 'Possible'
else: ans = 'Impossible'
print(ans)