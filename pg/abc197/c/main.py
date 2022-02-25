from itertools import product

N = int(input())
A = list(map(int, input().split()))

ans = sum(A)

for bits in product([0, 1], repeat=N-1):
    a, tmp = 0, 0

    for i in range(N):
        tmp |= A[i]
        if i == N-1 or bits[i]:
            a ^= tmp
            tmp = 0
    
    ans = min(ans, a)

print(ans)