from bisect import bisect_left
n = int(input())
x = list(map(int, input().split()))
xs = sorted(x)
for i in range(n):
    xi = x[i]
    if bisect_left(xs, xi) <= n//2 - 1: ans = xs[n//2]
    else: ans = xs[n//2 - 1]
    print(ans)