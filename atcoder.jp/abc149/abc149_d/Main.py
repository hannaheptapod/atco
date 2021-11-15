n, k = map(int, input().split())
r, s, p = map(int, input().split())
d = {'r':p, 's':r, 'p':s}
t = input()
ans = 0
for i in range(k):
    now = ''
    cnt = 0
    for j in range(i, n, k):
        tj = t[j]
        if tj != now:
            now = tj
            cnt = 0
            ans += d[tj]
        elif cnt%2 == 0: ans += d[tj]
        cnt += 1
print(ans)