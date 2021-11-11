from collections import deque
s = deque(input().split())
f = 1
for _ in range(int(input())):
    qi = list(input().split())
    if int(qi[0]) == 1: f = 3-f
    elif int(qi[1]) == f: s.appendleft(qi[2])
    else: s.append(qi[2])
s = ''.join(s)
if f == 2: s = s[::-1]
print(s)