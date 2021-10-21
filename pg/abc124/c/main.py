s = input()
a1 = a2 = 0
for i in range(len(s)):
    if i % 2:
        if s[i] == '0': a1 += 1
        else: a2 += 1
    else:
        if s[i] == '1': a1 += 1
        else: a2 += 1
ans = min(a1, a2)
print(ans)