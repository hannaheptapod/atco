N, D = map(int, input().split())
LR = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])

ans = 0
prev = -D
for l, r in LR:
    if prev + D - 1 < l:
        ans += 1
        prev = r

print(ans)
