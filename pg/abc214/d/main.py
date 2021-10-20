n = int(input())
uvw = [list(map(int, input().split())) for _ in range(n - 1)]
ans = 0

for i in range(1, n):
    for j in range(i+1, n+1):
        tmp = 0
        ans += tmp
print(ans)