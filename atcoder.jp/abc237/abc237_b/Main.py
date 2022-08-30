H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [[A[i][j] for i in range(H)] for j in range(W)]

_ = [print(*bi) for bi in B]
