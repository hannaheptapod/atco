s = input()
k = int(input())
tmp, lng = s[0], 0
ls = []
for si in s:
    if si == tmp: lng += 1
    else:
        ls.append(lng)
        tmp, lng = si, 1
ls.append(lng)
if len(ls) == 1: ans = ls[0]*k // 2
else:
    ans = k * sum(lsi//2 for lsi in ls)
    if s[-1] == s[0]: ans += (k-1) * ((ls[0]+ls[-1])//2 - ls[0]//2 - ls[-1]//2)
print(ans)