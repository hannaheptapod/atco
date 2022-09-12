def pow_mod(a, n, mod=MOD):
    if not n: return 1
    return (a*pow_mod(a, n-1) if n%2 else pow_mod(a**2%mod, n>>1))%mod
