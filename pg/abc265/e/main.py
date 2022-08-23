from itertools import combinations_with_replacement

MOD = 998244353

N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())

isPar = [
    A*D-B*C != 0 or A == B == 0 or C == D == 0,
    C*F-D*E != 0 or C == D == 0 or E == F == 0,
    E*B-F*A != 0 or E == F == 0 or A == B == 0
]

dic = {}
for ci in combinations_with_replacement(range(N+1), 3):
    x, y, z = ci[0], ci[1]-ci[0], ci[2]-ci[1]

    dic[(A*x + C*y + E*z, B*x + D*y + F*z)] = N - (x + y + z)

ans = 3**N % MOD
for _ in range(M):
    X, Y = map(int, input().split())

    if (X, Y) in dic: ans = (ans-3**dic[(X, Y)])%MOD

print(ans)
