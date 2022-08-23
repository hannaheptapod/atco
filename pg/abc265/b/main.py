N, M, T = map(int, input().split())
A = list(map(int, input().split()))

bonus = {}
for _ in range(M):
    x, y = map(int, input().split())

    bonus[x-1] = y

time = T
for i in range(N-1):
    time -= A[i]
    if i in bonus: time += bonus[i]

    if time <= 0:
        ans = 'No'
        break
else: ans = 'Yes'

print(ans)
