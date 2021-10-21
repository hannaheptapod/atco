n, m = map(int, input().split())
food = [0]*m
for _ in range(n):
    l = list(map(int, input().split()))
    for i in range(l[0]):
        food[l[i + 1] - 1] += 1
ans = 0
for fi in food:
    if fi == n: ans += 1
print(ans)