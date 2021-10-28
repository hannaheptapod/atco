n = int(input())
inner = fb = la = fbla = 0
for _ in range(n):
    s = input()
    l = len(s)
    for i in range(l - 1):
        if s[i:i+2] == 'AB': inner += 1
    fb += int(s[0] == 'B' and s[-1] != 'A')
    la += int(s[0] != 'B' and s[-1] == 'A')
    fbla += int(s[0] == 'B' and s[-1] == 'A')
if fbla == 0: outer = min(fb, la)
else:
    if fb + la > 0: outer = fbla + min(fb, la)
    else: outer = fbla - 1
ans = inner + min(outer, n - 1)
print(ans)