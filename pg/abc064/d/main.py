n, s = int(input()), input()

cnt = mn = 0

for si in s:
    if si == '(': cnt += 1
    else: cnt -= 1

    if cnt < mn: mn = cnt

s = '('*abs(mn) + s + ')'*max(0, cnt-mn)

print(s)