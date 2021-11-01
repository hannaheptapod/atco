from collections import deque
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
for i in range(1, 2*n, 2): ans += a[i]
print(ans)