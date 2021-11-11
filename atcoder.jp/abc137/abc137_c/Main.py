n = int(input())
d = {}
for _ in range(n):
    s = input()
    ss = ''.join(sorted(s))
    if ss not in d: d[ss] = 0
    d[ss] += 1
ans = 0
for di in d: ans += d[di]*(d[di]-1)//2
print(ans)