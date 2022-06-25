N = int(input())
S = input()
W = list(map(int, input().split()))
cmp = sorted(set(W))
dic = {cmp[i]: i for i in range(len(cmp))}
arr = sorted([[dic[W[i]], int(S[i])] for i in range(N)])

cnt = {i: [0, 0] for i in range(len(cmp))}
for w, s in arr:
    if s: cnt[w][1] += 1
    else: cnt[w][0] += 1

sm = [[0, N]]
for i in range(len(cmp)):
    sm.append([sm[-1][0]+cnt[i][0], sm[-1][1]+cnt[i][1]])

ans = 0
for x, y in sm: ans = max(ans, x + sm[-1][-1]-y)
print(ans)
