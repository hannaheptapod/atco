n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    xi, yi = p[i]
    for j in range(i+1, n):
        xj, yj = p[j]
        ans += ((xi-xj)**2 + (yi-yj)**2)**0.5
ans = ans*2 / n
print(ans)