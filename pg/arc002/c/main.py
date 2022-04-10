from itertools import combinations, product

N = int(input())
c = input() + '.'

ans = N
for l, r in combinations(map(''.join, product('ABXY', repeat=2)), 2):
    cnt, id = 0, 0
    while id < N:
        cnt += 1
        id += 2 if c[id:id+2] in (l, r) else 1

    ans = min(ans, cnt)

print(ans)
