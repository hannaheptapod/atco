from bisect import bisect_left as bil

N, M, Q = map(int, input().split())
pkg = [list(map(int, input().split())) for _ in range(N)]
pkg.sort(key=lambda x: x[1], reverse=True)
X = list(map(int, input().split()))

for _ in range(Q):
    l, r = map(int, input().split())
    box = sorted(X[:l-1] + X[r:])

    ans = 0
    for (w_i, v_i) in pkg:
        id = bil(box, w_i)

        if id < len(box):
            box.pop(id)

            ans += v_i

    print(ans)
