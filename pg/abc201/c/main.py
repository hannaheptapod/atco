s = input()
ans = 0
for n in range(10**4):
    n = '{:04}'.format(n)
    for i in range(10):
        si = s[i]
        if si == 'o' and str(i) not in n: break
        if si == 'x' and str(i) in n: break
    else: ans += 1
print(ans)