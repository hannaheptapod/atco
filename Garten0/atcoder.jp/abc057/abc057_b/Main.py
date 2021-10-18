n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

def closest(i):
    a, b = ab[i]
    dst = 10**10
    res = 0
    for j in range(m):
        c, d = cd[j]
        tmp = abs(a - c) + abs(b - d)
        if tmp < dst:
            dst = tmp
            res = j + 1
    return res

_ = [print(closest(i)) for i in range(n)]