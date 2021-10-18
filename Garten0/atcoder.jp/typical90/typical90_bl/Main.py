n, q = map(int, input().split())
a = list(map(int, input().split()))
gap = [a[i + 1] - a[i] for i in range(n - 1)]
inc = sum([abs(g) for g in gap])
for _ in range(q):
    l, r, v = map(int, input().split())
    if l > 1:
        inc -= abs(gap[l - 2])
        gap[l - 2] += v
        inc += abs(gap[l - 2])
    if r < n:
        inc -= abs(gap[r - 1])
        gap[r - 1] -= v
        inc += abs(gap[r - 1])
    print(inc)