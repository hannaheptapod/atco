n = int(input())
a = list(map(int, input().split()))
a.sort()
q = int(input())
for i in range(q):
    b = int(input())
    lo = 0
    hi = n - 1
    while hi - lo > 1:
        mi = (lo + hi) // 2
        ai = a[mi]
        if b <= ai:
            hi = mi
        if b >= ai:
            lo = mi
    ans = min(abs(b - a[lo]), abs(b - a[hi]))
    print(ans)