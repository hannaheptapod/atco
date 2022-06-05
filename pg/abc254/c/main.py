N, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)

for i in range(K):
    s = sorted(A[i::K])
    for j in range(i, N, K): A[j] = s[j//K]

ans = 'Yes' if A == B else 'No'
print(ans)
