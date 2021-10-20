from collections import deque as dq
d = dq()
q = int(input())
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        d.appendleft(x)
    elif t == 2:
        d.append(x)
    else:
        ans = d[x - 1]
        print(ans)