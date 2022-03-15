H, W, K = map(int, input().split())
s = [input() for _ in range(H)]

ans = [[0]*W for _ in range(H)]
cnt = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            cnt += 1
            ans[i][j] = cnt

for i in range(H):
    for j in range(1, W):
        if not ans[i][j]: ans[i][j] = ans[i][j-1]
    for j in range(W-2, -1, -1):
        if not ans[i][j]: ans[i][j] = ans[i][j+1]
for j in range(W):
    for i in range(1, H):
        if not ans[i][j]: ans[i][j] = ans[i-1][j]
    for i in range(H-2, -1, -1):
        if not ans[i][j]: ans[i][j] = ans[i+1][j]

_ = [print(*ai) for ai in ans]
