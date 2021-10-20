s = input()
t = input()
ans = 'No'
if s == t: ans = 'Yes'
else:
    n = []
    l = len(s)
    for i in range(l):
        if s[i] != t[i]: n.append(i)
    if len(n) == 2 and n[1]-n[0] == 1:
        if s[n[0]] == t[n[1]] and s[n[1]] == t[n[0]]: ans = 'Yes'
        ense: ans = 'No'
print(ans)