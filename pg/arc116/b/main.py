MOD = 998244353
N = int(input())
A = sorted(map(int, input().split()), reverse=True)

ans = A[0]**2 % MOD
ai = A[0]

for i in range(1, N):
    ai = (2*(ai - A[i-1]) + A[i-1] + A[i]) % MOD
    ans = (ans + A[i]*ai) % MOD

print(ans)
