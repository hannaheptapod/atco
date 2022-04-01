S = input()

if len(S) <= 2:
    if int(S)%8 and int(S[::-1])%8: ans = 'No'
    else: ans = 'Yes'
else:
    dic_s = {str(i): 0 for i in range(10)}
    for si in S: dic_s[si] += 1

    for tail in range(112, 10**3, 8):
        t = str(tail)
        dic = dic_s.copy()

        for ti in t:
            dic[ti] -= 1
            if dic[ti] < 0: break
        else:
            ans = 'Yes'
            break
        continue
    else: ans = 'No'

print(ans)
