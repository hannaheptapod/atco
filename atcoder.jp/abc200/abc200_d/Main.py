N = int(input())
A = list(map(lambda x: int(x)%200, input().split()))

dp = [[] for _ in range(200)]
dp[A[0]].append(1)

for i in range(2, N+1):
    ai = A[i-1]

    if dp[ai]:
        ans = 'Yes'
        B = dp[ai]
        C = [i]
        break
    else: dp[ai] = [i]

    for j in range(200):
        if not dp[j] or dp[j][-1] == i: continue

        if dp[(ai+j)%200]:
            ans = 'Yes'
            B = dp[(ai+j)%200]
            C = dp[j] + [i]
            break
        else: dp[(ai+j)%200] = dp[j] + [i]

    else: continue
    break
else: ans = 'No'

print(ans)
if ans == 'Yes':
    print(len(B), *B)
    print(len(C), *C)
