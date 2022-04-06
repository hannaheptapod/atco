N, W = map(int, input().split())
diff = [0]*(2 * 10**5 + 1)
for _ in range(N):
    s, t, p = map(int, input().split())

    diff[s] += p
    diff[t] -= p

cu = 0
for di in diff:
    cu += di
    if cu > W:
        ans = 'No'
        break
else: ans = 'Yes'

print(ans)
