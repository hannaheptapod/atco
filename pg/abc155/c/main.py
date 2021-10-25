n = int(input())
l = []
cnt = []
for _ in range(n):
    s = input()
    if s not in l:
        l.append(s)
        cnt.append(1)
    else: cnt[l.index(s)] += 1
mx = max(cnt)
ans = []
for i in range(len(l)):
    if cnt[i] == mx: ans.append(l[i])
ans.sort()
_ = [print(ai) for ai in ans]