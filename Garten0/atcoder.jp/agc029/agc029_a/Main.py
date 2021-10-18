s = input()
bs = 0
ans = 0
for si in s:
    if si == 'B': bs += 1
    else: ans += bs
print(ans)