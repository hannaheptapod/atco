x, y = map(int, input().split())
MOD = 10**9 + 7

def ncr(n, r):
    top = b1 = b2 = 1

    for i in range(n, 0, -1): top = top*i % MOD
    for j in range(n-r, 0, -1): b1 = b1*j % MOD
    for k in range(r, 0, -1): b2 = b2*k % MOD

    return top*pow(b1, -1, mod=MOD)*pow(b2, -1, mod=MOD) % MOD

if (x+y)%3: ans = 0
elif max(x, y) > 2*min(x, y): ans = 0
else:
    n = (x+y)//3
    r = x - (x+y)//3
    ans = ncr(n, r)

print(ans)