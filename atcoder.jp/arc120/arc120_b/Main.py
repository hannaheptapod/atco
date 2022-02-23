H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 998244353

board = [set() for _ in range(H + W - 1)]

for i in range(H):
    for j in range(W):
        if S[i][j] != '.': board[i+j].add(S[i][j])

ans = 1
for bi in board: ans = ans*(2 - len(bi))%MOD

print(ans)