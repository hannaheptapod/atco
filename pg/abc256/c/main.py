from itertools import combinations

h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for c1 in combinations(range(h1-1), 2):
    r1 = [c1[0]+1, c1[1]-c1[0], h1-c1[1]-1]

    for c2 in combinations(range(h2-1), 2):
        r2 = [c2[0]+1, c2[1]-c2[0], h2-c2[1]-1]

        r3 = [w1-r1[0]-r2[0], w2-r1[1]-r2[1], w3-r1[2]-r2[2]]

        if min(r3) > 0 and sum(r3) == h3: ans += 1

print(ans)
