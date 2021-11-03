s = input()
ans = ''
for si in s:
    if si != 'B': ans += si
    else: ans = ans[:max(len(ans)-1, 0)]
print(ans)