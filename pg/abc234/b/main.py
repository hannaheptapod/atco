N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-1):
    xi, yi = xy[i]
    for j in range(i+1, N):
        xj, yj = xy[j]

        ans = max(ans, ((xi-xj)**2 + (yi-yj)**2)**0.5)

print(ans)
