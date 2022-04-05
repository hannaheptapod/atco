from collections import deque
S = input()

t = deque()
rev = False
for si in S:
    if si == 'R': rev = not rev
    elif not t: t.append(si)
    elif not rev:
        r = t.pop()
        if r != si:
            t.append(r)
            t.append(si)
    else:
        l = t.popleft()
        if l != si:
            t.appendleft(l)
            t.appendleft(si)

ans = ''
while t: ans += t.popleft()
if rev: ans = ans[::-1]

print(ans)
