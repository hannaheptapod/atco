from bisect import bisect_left as bil

N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
i, j = 0, 0
while i < N:
    j = bil(b, a[i]+X)
    if j >= M: break

    i = bil(a, b[j]+Y)
    ans += 1

print(ans)
