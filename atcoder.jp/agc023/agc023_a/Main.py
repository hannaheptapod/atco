N = int(input())
A = list(map(int, input().split()))
S = [0]
for ai in A: S += [S[-1] + ai]
S.sort()

ans = 0
tmp, cnt = 0, 0

for si in S:
    if si == tmp: cnt += 1
    else:
        ans += cnt*(cnt-1) // 2
        tmp, cnt = si, 1
ans += cnt*(cnt-1) // 2

print(ans)