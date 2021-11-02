n, m = map(int, input().split())
store = [list(map(int, input().split())) for _ in range(n)]
store.sort()
ans = 0
for i in range(n):
    if store[i][1] >= m:
        ans += store[i][0]*m
        break
    else:
        ans += store[i][0]*store[i][1]
        m -= store[i][1]
print(ans)