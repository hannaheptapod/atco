import bisect
l, q = map(int, input().split())
cut = [0, l]
for _ in range(q):
    c, x = map(int, input().split())

    if c == 1:
        bisect.insort(cut, x)
    else:
        pos = bisect.bisect(cut, x)
        ans = cut[pos] - cut[pos - 1]
        print(ans)