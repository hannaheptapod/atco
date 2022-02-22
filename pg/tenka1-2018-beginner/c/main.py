N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()

sm_s, sm_l = sum(A[:N//2]), sum(A[N//2:])

if N%2: ans = 2*(sm_l - sm_s) - min(A[N//2]+A[N//2 + 1], 3*A[N//2]-A[N//2 - 1])
else: ans = 2*(sm_l - sm_s) - (A[N//2]-A[N//2 - 1])

print(ans)