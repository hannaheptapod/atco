s = input()
l, r = s.find('A'), s[::-1].find('Z')
ans = len(s) - l - r
print(ans)