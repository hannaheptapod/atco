from collections import deque

n, m = map(int, input().split())
a = [deque() for _ in range(m)]
donde = [[] for _ in range(n)]
top = [0] * n
que = deque()

for i in range(m):
    k = int(input())
    ai = list(map(int, input().split()))

    for aij in ai:
        a[i].appendleft(aij - 1)
        donde[aij - 1].append(i)
    
    ti = a[i].pop()
    top[ti] += 1

for i in range(n): 
    if top[i] == 2: que.appendleft(i)

cnt = 0
while que:
    qi = que.pop()
    d1, d2 = donde[qi][0], donde[qi][1]
    cnt += 1
    if a[d1]:
        td1 = a[d1].pop()
        top[td1] += 1
        if top[td1] == 2: que.appendleft(td1)
    if a[d2]:
        td2 = a[d2].pop()
        top[td2] += 1
        if top[td2] == 2: que.appendleft(td2)

if cnt == n: ans = 'Yes'
else: ans = 'No'

print(ans)