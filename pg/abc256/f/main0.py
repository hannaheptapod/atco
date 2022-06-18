MOD = 998244353

N, Q = map(int, input().split())
A = list(map(int, input().split()))


def nc2(n): return n*(n+1)//2


B = [A[0]%MOD]
for ai in A[1:]: B.append((B[-1]+ai) % MOD)
C = [B[0]%MOD]
for bi in B[1:]: C.append((C[-1]+bi) % MOD)
ans = [C[0]%MOD]
for ci in C[1:]: ans.append((ans[-1]+ci) % MOD)


for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        diff = query[2] - A[query[1]-1]

        for i in range(query[1]-1, N):
            ans[i] += diff*nc2(i-query[1]+2)
            ans[i] %= MOD

        A[query[1]-1] = query[2]

    else: print(ans[query[1]-1])
