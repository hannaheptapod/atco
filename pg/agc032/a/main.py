from collections import deque
n = int(input())
b = list(map(int, input().split()))
d = deque()
for i in range(n):
    tmp = -1
    for j in range(n-i):
        if b[j] == j+1: tmp = j
    if tmp > -1:
        d.appendleft(b[tmp])
        b.pop(tmp)
    else:
        print(-1)
        break
else:
    while d: print(d.popleft())