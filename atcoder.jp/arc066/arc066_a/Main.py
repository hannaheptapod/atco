n = int(input())
a = list(map(int, input().split()))

def pow2(x):
    mod = 10**9 + 7
    res = 1
    dos = 2
    while x:
        if x & 1:
            res = res*dos % mod
        dos = dos*dos % mod
        x >>= 1
    return res

if n%2: d = {i:0 for i in range(0, n, 2)}
else: d = {i:0 for i in range(1, n, 2)}

ans = 0

for ai in a:
    if ai not in d: break
    elif ai == 0 and d[ai] >= 1: break
    elif d[ai] >= 2: break
    else: d[ai] += 1
else: ans = pow2(n//2)

print(ans)