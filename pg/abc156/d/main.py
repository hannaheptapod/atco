n, a, b = map(int, input().split())

MOD = 10**9 + 7

def dos(r):
    tmp, d = 1, 2

    while r:
        if r%2: tmp = tmp*d % MOD
        d = d**2 % MOD
        r >>= 1
    
    return tmp

def comb(n, r):
    res = 1

    for i in range(r): res = res*(n-i)*pow(i+1, -1, mod=MOD) % MOD

    return res

ans = (dos(n)-1 - (comb(n, a)+comb(n, b))) % MOD

print(ans)