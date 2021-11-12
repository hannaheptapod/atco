from collections import deque
n = int(input())
d = deque()
for _ in range(n): d.append(tuple(map(int, input().split())))
ans = 0
for _ in range(n):
    a, b = d.pop()
    ans += -(a + ans)%b
print(ans)