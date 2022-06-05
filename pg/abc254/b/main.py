N = int(input())

comb = [[0]*i for i in range(1, N+1)]
for i in range(N):
    comb[i][0] = comb[i][-1] = 1

    for j in range(1, i): comb[i][j] = comb[i-1][j-1]+comb[i-1][j]

_ = [print(*ci) for ci in comb]
