N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

cu = [0]*(N+1)
for i in range(N): cu[i+1] = cu[i] + A[i]

st = set(cu)
for c in cu:
    if c+P in st and c+P+Q in st and c+P+Q+R in st:
        ans = 'Yes'
        break
else: ans = 'No'

print(ans)
