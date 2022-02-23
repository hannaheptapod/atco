import bisect, array

L, Q = map(int, input().split())
cut = array.array('i', [0, L])

for _ in range(Q):
    c, x = map(int, input().split())

    pos = bisect.bisect(cut, x)

    if c == 1: cut.insert(pos, x)
    else: print(cut[pos] - cut[pos - 1])