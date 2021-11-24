from collections import deque
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dq = deque(sorted([a[i]-b[i] for i in range(n)]))
ans = 0
sm = 0
while dq:
    di = dq.popleft()
    if di < 0:
        ans += 1
        sm += di
    else:
        dq.appendleft(di)
        break
while dq and sm < 0:
    di = dq.pop()
    ans += 1
    sm += di
if sm < 0: ans = -1
print(ans)