n = int(input())
l0, l1 = 2, 1
if n == 1: ans = l1
else:
    for _ in range(n - 1):
        t0, t1 = l0, l1
        l0 = t1
        l1 = t0 + t1
    ans = l1
print(ans)