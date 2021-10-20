s = input()
n = len(s)
t, b = [], []
if s[0] == '>': t += [0]
else: b += [0]
for i in range(n - 1):
    if s[i:i+2] == '<>': t += [i+1]
    elif s[i:i+2] == '><': b += [i+1]
if s[-1] == '<': t += [n]
else: b += [n]
m = len(t)
ans = 0
if t[0] != 0:   
    for i in range(m - 1):
        l, r = t[i] - b[i], b[i+1] - t[i]
        ans += l*(l+1)//2 + r*(r+1)//2 - min(l, r)
    l = t[-1] - b[m-1]
    if t[-1] != n: r = b[-1] - t[-1]
    else: r = 0
    ans += l*(l+1)//2 + r*(r+1)//2 - min(l, r)
else:
    r = b[0] - t[0]
    ans += r*(r+1)//2
    for i in range(1, m - 1):
        l, r = t[i] - b[i-1], b[i] - t[i]
        ans += l*(l+1)//2 + r*(r+1)//2 - min(l, r)
    l = t[-1] - b[m-2]
    if t[-1] != n: r = b[-1] - t[-1]
    else: r = 0
    if m > 1: ans += l*(l+1)//2 + r*(r+1)//2 - min(l, r)
print(ans)