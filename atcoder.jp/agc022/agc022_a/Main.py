s = input()
abc = 'abcdefghijklmnopqrstuvwxyz'
if len(s) < 26:
    for abci in abc:
        if abci not in s:
            ans = s + abci
            break
else:
    t = [s[-1]]
    for i in range(2, 26+1):
        if s[-i] > t[-1]: t.append(s[-i])
        else: break
    if len(t) == 26: ans = -1
    else:
        for ti in t:
            if ti > s[26-i]:
                ans = s[:26-i] + ti
                break
print(ans)