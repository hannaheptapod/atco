import bisect

N, Q = map(int, input().split())
A = sorted(map(int, input().split()))

cu = [0]*(N+1)
for i in range(N): cu[i+1] = cu[i]+A[i]

for _ in range(Q):
    X = int(input())

    b = bisect.bisect_left(A, X)

    ans = X*b-cu[b] + (cu[-1]-cu[b])-X*(N-b)
    print(ans)
