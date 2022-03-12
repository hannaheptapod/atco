N, X = map(int, input().split())
S = input()

ls = [[S[0], 1]]
for si in S[1:]:
    if si == ls[-1][0]:
        ls[-1][1] += 1
    else:
        ls += [[si, 1]]

last = 0
for i in range(len(ls)):
    if ls[i][0] == 'U':
        for j in range(i-1, last, -1):
            if ls[j][1] <= ls[i][1]:
                ls[j][1], ls[i][1] = 0, ls[i][1] - ls[j][1]
            else:
                ls[j][1], ls[i][1] = ls[j][1] - ls[i][1], 0
                break
        last = i


def pow(x, p):
    y = 1

    while p:
        if p % 2:
            y *= x

        x *= x
        p >>= 1

    return y


now = X
r, sm = 0, 0
for li in ls:
    d, p = li
    if not p:
        continue

    if d == 'U':
        now = now*pow(2, sm) + r
        r, sm = 0, 0

        now //= pow(2, p)

    elif d == 'L':
        r *= pow(2, p)
        sm = p
    else:
        r *= pow(2, p)
        r += pow(2, p)-1
if sm:
    now = now*pow(2, sm) + r

ans = now
print(ans)
