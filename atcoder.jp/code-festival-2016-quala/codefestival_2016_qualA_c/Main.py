from string import ascii_lowercase as abc

s = input()
k = int(input())

dst = {abc[i]:(26-i)%26 for i in range(26)}

ans = ''
i = 0

while i < len(s):
    si = s[i]
    di = dst[si]

    if i == len(s)-1: ans += abc[(abc.index(si) + k)%26]
    elif di <= k:
        ans += 'a'
        k -= di
    elif not k: 
        ans += s[i:-1]
        i = len(s)-1
        continue
    else: ans += si

    i += 1

print(ans)