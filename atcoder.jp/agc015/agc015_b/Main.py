s = input()
smu = -int(s[0] == 'U') + sum([int(si == 'U') for si in s])
ls = len(s)
ans = ls*(ls-1)
for i in range(ls-1):
    if s[i] == 'D': ans += ls-i-1
    ans += smu
    smu -= int(s[i+1] == 'U')
print(ans)