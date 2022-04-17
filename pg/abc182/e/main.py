import array

H, W, N, M = map(int, input().split())

board = [array.array('i', [-1]*(W+2))] +\
    [array.array('i', [-1]+[0]*W+[-1]) for _ in range(H)] +\
    [array.array('i', [-1]*(W+2))]
for _ in range(N):
    a, b = map(int, input().split())
    board[a][b] = 1

ans = 0
for _ in range(M):
    c, d = map(int, input().split())
    if board[c][d]: continue
    board[c][d] =
