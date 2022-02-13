import re

s = input()

t = ''
flag = False

for si in s:
    if flag:
        if si == 'A':
            t += 'BA'
            flag = False
        elif si == 'B': t += 'B'
        else:
            t += 'X'
            flag = False

    else:
        if si == 'A': t += 'A'
        elif si == 'B': flag = True
        else: t += 'C'
if flag: t += 'B'

lt = list(re.split('[BC]', t))
ans = 0

for ti in lt:
    cnt = 0
    for tij in ti:
        if tij == 'A': cnt += 1
        else: ans += cnt

print(ans)