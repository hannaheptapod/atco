h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

ans = 0

for a in range(1<<h):
    ys = [False] * h
    for i in range(h):
        if a % 2: ys[i] = True
        a >>= 1
    for b in range(1<<w):
        cnt = 0
        xs = [False] * w
        for j in range(w):
            if b % 2: xs[j] = True
            b >>= 1
        for i in range(h):
            for j in range(w):
                if ys[i] and xs[j] and c[i][j] == '#': cnt += 1
            if cnt > k: break
        else:
            if cnt == k: ans += 1
print(ans)