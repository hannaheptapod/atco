N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [1, 1]
for i in range(N-1):
    nxt = [0, 0]

    if dp[0]:
        if abs(A[i+1]-A[i]) <= K: nxt[0] = 1
        if abs(B[i+1]-A[i]) <= K: nxt[1] = 1
    if dp[1]:
        if abs(A[i+1]-B[i]) <= K: nxt[0] = 1
        if abs(B[i+1]-B[i]) <= K: nxt[1] = 1

    if sum(nxt): dp = nxt
    else:
        ans = 'No'
        break
else: ans = 'Yes'

print(ans)
