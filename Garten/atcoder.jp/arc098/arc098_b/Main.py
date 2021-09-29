N = int(input())
A = list(map(int, input().split()))
xo = [a for a in A]
sm = [a for a in A]

for i in range(1, N):
    xo[i] ^= xo[i-1]
    sm[i] += sm[i-1]

ans = 0
for i in range(N):
    ok = i
    ng = N
    while ok+1 != ng:
        md = (ok + ng) // 2
        x = xo[md]
        s = sm[md]
        if i:
            x ^= xo[i-1]
            s -= sm[i-1]
        if x==s:
            ok = md
        else:
            ng = md
    ans += ok - i + 1
print(ans)