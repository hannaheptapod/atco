X, A, D, N = map(int, input().split())

mn, mx = min(A, A+D*(N-1)), max(A, A+D*(N-1))

if X <= mn: ans = mn-X
elif X >= mx: ans = X-mx
else: ans = min((A-X)%abs(D), (X-A)%abs(D))

print(ans)
