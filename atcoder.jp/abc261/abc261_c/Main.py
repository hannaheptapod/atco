N = int(input())
S = [input() for _ in range(N)]

cnt = {}
for i in range(N):
    if S[i] not in cnt:
        ans = S[i]
        cnt[S[i]] = 1
    else:
        ans = S[i] + '(' + str(cnt[S[i]]) + ')'
        cnt[S[i]] += 1

    print(ans)
