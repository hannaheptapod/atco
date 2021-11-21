from bisect import bisect_left
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n-2):
    li = l[i]
    for j in range(i+1, n-1):
        lj = l[j]
        ans += max(bisect_left(l, li+lj)-(j+1), 0)
print(ans)