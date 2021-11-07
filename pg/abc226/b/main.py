n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()
ans = 1
for i in range(1, n):
    if a[i] != a[i-1]: ans += 1
print(ans)