from collections import deque
n = int(input())
a = list(map(str, input().split()))
b = deque()
for i in range(n):
    if (n-i)%2: b.appendleft(a[i])
    else: b.append(a[i])
print(*list(b))