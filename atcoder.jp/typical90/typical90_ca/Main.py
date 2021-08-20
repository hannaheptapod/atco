h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]
diff = [[aij - bij for aij, bij in zip(ai, bi)] for ai, bi in zip(a, b)]
cnt = 0
for i in range(h - 1):
    for j in range(w - 1):
        dij = diff[i][j]
        diff[i][j] -= dij
        diff[i][j+1] -= dij
        diff[i+1][j] -= dij
        diff[i+1][j+1] -= dij
        cnt += abs(dij)
    if diff[i][w-1]:
        print('No')
        break
else:
    print('Yes')
    print(cnt)