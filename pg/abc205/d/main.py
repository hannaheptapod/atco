from bisect import bisect_left as bil

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))

C = [A[i]-i for i in range(N+1)]

for _ in range(Q):
    K = int(input())

    if C[-1] < K: ans = A[-1] + (K - C[-1])
    else:
        id = bil(C, K)
        ans = (A[id] - 1) - (C[id] - K)

    print(ans)
