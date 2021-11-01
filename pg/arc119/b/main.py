n, s, t = int(input()), input(), input()
if s == t: ans = 0
else:
    ans = 0
    sl, tl = [], []
    for i in range(n):
        if s[i] == '0': sl.append(i)
        if t[i] == '0': tl.append(i)
    if len(sl) != len(tl): ans = -1
    else:
        for i in range(len(sl)): ans += int(sl[i] != tl[i])
print(ans)