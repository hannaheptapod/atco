s = input()
length = len(s)

if s == 'keyence': ans = 'YES'
else:
    for l in range(length + 1):
        left = s[:l]
        for r in range(l, length + 1):
            right = s[r:]
            if left + right == 'keyence':
                ans = 'YES'
                break
        else: continue
        break
    else: ans = 'NO'
print(ans)