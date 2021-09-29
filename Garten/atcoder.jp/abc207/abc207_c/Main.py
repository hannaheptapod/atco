N = int(input())
l, r = [0]*N, [0]*N
for i in range(N):
    t, l[i], r[i] = map(int, input().split())
    if t%2 == 0:
        r[i] -= 0.5
    if t>2:
        l[i] += 0.5
ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans += (max(l[i], l[j]) <= min(r[i], r[j]))
print(ans)