n = int(input())
a, b = [], []
for _ in range(n):
    ab = list(map(int, input().split()))
    a.append(ab[0])
    b.append(ab[1])
amin = min(a)
bmin = min(b)
am_i = a.index(amin)
bm_i = b.index(bmin)
ans = max(amin, bmin)
if am_i == bm_i:
    a.sort()
    b.sort()
    if a[0] != a[1] and b[0] != b[1]:
        ans = min(a[0]+b[0], max(a[0], b[1]), max(a[1], b[0]))
print(ans)