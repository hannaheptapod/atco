n = int(input())
a = list(map(int, input().split()))
ans = [0]*n
hi = lo = n-1
for i in range(n-2, -1, -1):
    if a[i] > a[hi]: hi = i
    elif hi < lo:
        ans[hi] = ans[lo] = 1
        hi = lo = i
    else: hi = lo = i
if hi < lo: ans[hi] = ans[lo] = 1
print(*ans)