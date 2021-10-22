s = input()
a, c = s.find('A'), s.find('C')
alpha = 'abcdefghijklmnopqrstuvwxyz'
if a != 0: ans = 'WA'
elif c < 2 or c > len(s) - 2: ans = 'WA'
else:
    for i in range(1, len(s)):
        if i == c: continue
        elif s[i] not in alpha:
            ans = 'WA'
            break
    else: ans = 'AC'
print(ans)