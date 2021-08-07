def cvt(c):
    if c == '#':
        return 1
    else:
        return 0
H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for r in range(H - 1):
    for c in range(W - 1):
        if sum(map(cvt, [S[r][c], S[r][c+1], S[r+1][c], S[r+1][c+1]]))%2 == 1:
            ans += 1
print(ans)
