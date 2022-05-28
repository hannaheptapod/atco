H, W = map(int, input().split())
S = [input() for _ in range(H)]

nbh = range(-1, 2)
ans = [['#']*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#': continue

        for di in nbh:
            if i+di < 0 or i+di >= H: continue

            for dj in nbh:
                if j+dj < 0 or j+dj >= W: continue

                ans[i+di][j+dj] = '.'

for i in range(H):
    for j in range(W):
        if S[i][j] == '.': continue

        for di in nbh:
            if i+di < 0 or i+di >= H: continue

            for dj in nbh:
                if j+dj < 0 or j+dj >= W: continue

                if ans[i+di][j+dj] == '#': break
            else: continue
            break
        else:
            print('impossible')
            break
    else: continue
    break
else:
    print('possible')
    _ = [print(''.join(ai)) for ai in ans]
