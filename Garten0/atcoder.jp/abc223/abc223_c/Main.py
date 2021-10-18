n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
c = []
sm = [0]
for abi in ab:
    a, b = abi
    c.append(a/b)
    sm.append(sm[-1] + a/b)
md = sm[-1] / 2
ans = 0
for i in range(1, n+1):
    if sm[i] >= md:
        ans += (md - sm[i-1])*ab[i-1][1]
        break
    else: ans += ab[i-1][0]
print(ans)