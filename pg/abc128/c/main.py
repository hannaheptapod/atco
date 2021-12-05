n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
for x in range(2**n):
    xbi = bin(x)[2:]
    while len(xbi) < n: xbi = '0' + xbi
    for i in range(m):
        si = s[i]
        cnt = 0
        for j in range(si[0]): cnt += int(xbi[si[j+1]-1] == '1')
        if cnt%2 != p[i]: break
    else: ans += 1
print(ans)