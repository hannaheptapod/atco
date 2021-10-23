from bisect import insort
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for _ in range(m):
    mx = a.pop(-1)
    insort(a, mx//2)
ans = sum(a)
print(ans)