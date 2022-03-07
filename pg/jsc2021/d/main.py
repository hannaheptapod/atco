N, P = map(int, input().split())
MOD = 10**9 + 7

ans = (P - 1)*pow(P - 2, N - 1, MOD) % MOD
print(ans)
