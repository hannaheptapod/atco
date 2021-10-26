s = input()
t = input()
ans = set()
ls, lt = len(s), len(t)
for i in range(ls - lt + 1):
    si = s[i:i + lt]
    if all([si[j] == '?' or si[j] == t[j] for j in range(lt)]): ai = t
    else: continue
    l, r = '', ''
    for j in range(i):
        if s[j] == '?': l += 'a'
        else: l += s[j]
    for j in range(i + lt, ls):
        if s[j] == '?': r += 'a'
        else: r += s[j]
    ai = l + ai + r
    ans.add(ai)
if len(ans): print(sorted(ans)[0])
else: print('UNRESTORABLE')