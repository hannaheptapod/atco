import array
import bisect

N = int(input())
S = 'x' + input() + 'xxx'

arc = array.array('i', [])
for i in range(1, N+1):
    if S[i] != 'R': continue

    tmp = 0
    for j in range(1, i):
        if S[i-j] != 'A' or S[i+j] != 'C': break
        else: tmp += 1

    if tmp: bisect.insort(arc, tmp)

ans = 0
for i in range(1, N):
    if not any(arc): break
    ans += 1

    if i%2:
        arc[-1] -= 1
        if len(arc) >= 2 and arc[-1] < arc[-2]:
            r = arc.pop()
            if r: bisect.insort(arc, r)
    else: arc.pop(0)

print(ans)
