import bisect
n = int(input())
a, b = [0]*n, [0]*n
for i in range(n):
    ai, bi = map(int, input().split())
    a[i] = ai
    b[i] = ai + bi
a.sort()
b.sort()
sx = set(a + b)
x = list(sx)
x.sort()
k = len(x)
ans = [0] * (n+1)
cnt = 0
for i in range(k-1):
    na = bisect.bisect_right(a, x[i]) - bisect.bisect_left(a, x[i])
    nb = bisect.bisect_right(b, x[i]) - bisect.bisect_left(b, x[i])
    cnt += na - nb
    ans[cnt] += x[i+1] - x[i]
print(*ans[1:])