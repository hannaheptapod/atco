N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

ans = int(D[0] == 0)

for i in range(1, N): ans = ans*D[i]%MOD

print(ans)