from collections import Counter

N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

ans = 1
q = Counter(D)
if q[0] != 1 or D[0]: ans = 0
else:
    for i in range(1, max(D)+1): ans = ans*pow(q[i-1], q[i], MOD)%MOD

print(ans)