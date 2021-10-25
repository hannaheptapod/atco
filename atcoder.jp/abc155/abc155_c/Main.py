n = int(input())
d = {}
mx = 1
for _ in range(n):
    s = input()
    if s not in d: d[s] = 1
    else:
        d[s] = d[s] + 1
        if d[s] > mx: mx = d[s]
ans = []
for di in d:
    if d[di] == mx: ans.append(di)
ans.sort()
_ = [print(ai) for ai in ans]