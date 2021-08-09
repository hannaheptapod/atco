N = int(input())
S = input()
ans = -1
if S[0] != S[N - 1]:
    ans = 1
else:
    for i in range(1, N - 1):
        if S[0] != S[i] and S[0] != S[i + 1]:
            ans = 2
print(ans)