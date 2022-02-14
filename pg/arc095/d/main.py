from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split())) + [0]

a.sort()

ai = a[-1]

l = bisect_right(a, ai/2)-1
r = bisect_left(a, ai/2)

if a[l] >= ai-a[r]: aj = a[l]
else: aj = a[r]

ans = (ai, aj)

print(*ans)