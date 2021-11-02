s, t = map(list, [input() for _ in range(2)])
s.sort()
t.sort()
if s[0] < t[-1] or (len(s) < len(t) and s == t[:len(s)]): ans = 'Yes'
else: ans = 'No'
print(ans)