s = input()
n = len(s)
rx = s.find('<')
if rx == -1: r = n
else: r = rx
ans = r
for i in range(1, n):
    lx = s[:i].rfind('>')
    if lx == -1: l = i
    else: l = i - 1 - lx
    rx = s[i:].find('<')
    if rx == -1: r = n - i
    else: r = rx
    ans += max(l, r)
lx = s.rfind('>')
if lx == -1: l = n
else: l = n - 1 - lx
ans += l
print(ans)