s = input()
n = len(s)
dn = [0]*n
left = 0
for i in range(1, n):
    if s[i] == 'R':
        if s[i-1] == 'R': continue
        else: left = i
    else:
        if s[i-1] == 'R':
            for j in range(left, i):
                dn[j] = i
            left = i - 1
        dn[i] = left
dr = [dn[i] - i for i in range(n)]
ans = [0]*n
for i in range(n):
    if not dr[i] % 2: ans[dn[i]] += 1
    elif dr[i] > 0: ans[dn[i] - 1] += 1
    else: ans[dn[i] + 1] += 1
print(*ans)