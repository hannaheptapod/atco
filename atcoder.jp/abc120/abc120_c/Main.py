s = input()
r = sum([si == '0' for si in s])
b = len(s) - r
ans = 2 * min(r, b)
print(ans)