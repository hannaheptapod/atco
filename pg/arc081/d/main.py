MOD = 10**9 + 7
N = int(input())
S = [input() for _ in range(2)]

ans = 3 if S[0][0] == S[1][0] else 6
for i in range(1, N):
    if S[0][i] == S[0][i-1]: continue

    if S[0][i-1] == S[1][i-1]: ans *= 2
    elif S[0][i] != S[1][i]: ans *= 3

    ans %= MOD

print(ans)
