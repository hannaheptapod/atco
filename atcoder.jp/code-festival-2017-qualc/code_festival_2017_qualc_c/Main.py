s = input()

l, r = 0, len(s)-1
ans = 0

while l < r and ans != -1:
    if s[l] == s[r]:
        l += 1
        r -= 1
        continue
    
    ans += 1
    if s[l] == 'x': l += 1
    elif s[r] == 'x': r -= 1
    else: ans = -1

print(ans)