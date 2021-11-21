s = input()
t = s[0]
ans = 0
for si in s:
    if si != t:
        ans += 1
        t = si
print(ans)