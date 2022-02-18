from itertools import product

n = int(input())
test = [[] for _ in range(n)]
for i in range(n):
    ai = int(input())
    for _ in range(ai): test[i] += [list(map(int, input().split()))]

ans = 0

for p in product('01', repeat=n):
    for i in range(n):
        pi, ti = int(p[i]), test[i]

        if pi and any([tij[1] != int(p[tij[0]-1]) for tij in ti]): break
    else: ans = max(ans, sum([int(pi) for pi in p]))

print(ans)