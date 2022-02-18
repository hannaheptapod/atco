s = input()

ans = 0

for i in range(2**(len(s) - 1)):
    tmp = s[0]

    for j in range(1, len(s)):

        if i%2:
            ans += int(tmp)
            tmp = ''
        
        tmp += s[j]
        i >>= 1
    
    ans += int(tmp)

print(ans)