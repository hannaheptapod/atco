n, y = map(int,input().split())
ans = [-1]*3

for a in range(n + 1):
    an = 10000 * a
    for b in range(n - a + 1):
        bn = 5000 * b
        c = n - a - b
        cn = 1000 * c
        if sum([an, bn, cn]) == y:
            ans = [a, b, c]
            break
    else:
        continue
    break

print(*ans)