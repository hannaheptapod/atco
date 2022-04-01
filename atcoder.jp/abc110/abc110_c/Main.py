S, T = [input() for _ in range(2)]

f = [[False]*26 for _ in range(26)]
for i in range(len(S)): f[ord(S[i]) - ord('a')][ord(T[i])- ord('a')] = True

for i in range(26):
    cn = 0
    for j in range(26):
        if f[i][j]: cn += 1

    if 2 <= cn:
        ans = 'No'
        break
else:
    for j in range(26):
        cn = 0
        for i in range(26):
            if f[i][j]: cn += 1

        if 2 <= cn:
            ans = 'No'
            break
    else: ans = 'Yes'

print(ans)
