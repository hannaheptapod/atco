w = input()
s = tuple({wi for wi in w})
d = {s[i]: i for i in range(len(s))}
l = [0]*len(s)
for wi in w: l[d[wi]] += 1
for li in l:
    if li % 2:
        ans = 'No'
        break
else: ans = 'Yes'
print(ans)