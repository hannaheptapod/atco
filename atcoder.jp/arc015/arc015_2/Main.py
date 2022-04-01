N = int(input())
ans = [0]*6

for _ in range(N):
    mx, mn = map(float, input().split())

    if mx >= 35: ans[0] += 1
    elif mx >= 30: ans[1] += 1
    elif mx >= 25: ans[2] += 1

    if mn >= 25: ans[3] += 1

    if mn < 0 and mx >= 0: ans[4] += 1
    if mx < 0: ans[5] += 1

print(*ans)
