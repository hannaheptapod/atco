n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]

area = sorted([[x-l, x+l] for x, l in xl], key=lambda a: a[1])

ans, tmp = 0, -10**10
for ai in area:
    l, r = ai
    if l >= tmp:
        ans += 1
        tmp = r

print(ans)