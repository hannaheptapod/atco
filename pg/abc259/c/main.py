from collections import deque

S = input()
T = input()

ds, dt = deque(), deque()
for si in S:
    if not ds: ds.append([si, 1])
    else:
        last = ds.pop()
        if last[0] == si: last[1] += 1
        ds.append(last)
        if last[0] != si: ds.append([si, 1])
for ti in T:
    if not dt: dt.append([ti, 1])
    else:
        last = dt.pop()
        if last[0] == ti: last[1] += 1
        dt.append(last)
        if last[0] != ti: dt.append([ti, 1])

if len(ds) != len(dt): ans = 'No'
else:
    while ds:
        s, t = ds.popleft(), dt.popleft()
        if s[0] != t[0] or s[1] > t[1] or (s[1] == 1 and t[1] > 1):
            ans = 'No'
            break
    else: ans = 'Yes'

print(ans)
