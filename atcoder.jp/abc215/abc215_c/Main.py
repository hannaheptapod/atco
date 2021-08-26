import itertools
l = list(input().split())
s, k = list(l[0]), int(l[1])

s.sort()
slen = len(s)
snum = [0]
dic = {0: s[0]}
tmp = 0
for i in range(1, slen):
    if s[i] == s[i-1]: snum += [tmp]
    else:
        tmp += 1
        snum += [tmp]
        dic[tmp] = s[i]

per_s = set(itertools.permutations(snum))
per = list(per_s)
per.sort()
ans_l = [dic[pi] for pi in per[k-1]]
ans = ''.join(ans_l)

print(ans)