s = input()
prev = ''
cnt = []

for si in s:
    if si == prev: cnt[-1] += 1
    else:
        cnt += [si, 1]
        prev = si

ans = ''.join(map(str, cnt))
print(ans)
