N = int(input())
LR = sorted([list(map(int, input().split())) for _ in range(N)])

ans = []
l, r = LR[0]
for li, ri in LR[1:]:
    if r >= li: r = max(r, ri)
    else:
        ans.append([l, r])
        l, r = li, ri
if not ans or ans[-1] != [l, r]: ans.append([l, r])

_ = [print(*ai) for ai in ans]
