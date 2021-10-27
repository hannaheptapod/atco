s = input()
ans = 0
past = now = ''
for si in s:
    now += si
    if past != now:
        ans += 1
        past = now
        now = ''
print(ans)