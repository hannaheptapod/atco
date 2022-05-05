N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

mn = min([min(ci) for ci in C])
a, b = [ci[0] for ci in C], C[0]
A = [ai - min(a) for ai in a]
B = [bj - min(b) + mn for bj in b]

for i in range(N):
    for j in range(N):
        if C[i][j] == A[i] + B[j]: continue

        print('No')
        break
    else: continue
    break
else:
    print('Yes')
    print(*A)
    print(*B)
