N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for li in L:
    if (li < K or A[-1] < N) and A[li-1]+1 not in A: A[li-1] += 1

print(*A)
