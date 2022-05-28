H, W = map(int, input().split())
S = [input() for _ in range(H)]
x, y = [], []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            x.append(i)
            y.append(j)

ans = 0
if len(x) == 2: ans += abs(x[0]-x[1])
if len(y) == 2: ans += abs(y[0]-y[1])
print(ans)
