from itertools import permutations

N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]


if N < 3: ans = 1
else:
    ans = N
    for s, t in permutations(xy, 2):
        p, q = t[0] - s[0], t[1] - s[1]

        tmp = N
        for xi, yi in xy:
            if (xi + p, yi + q) in xy: tmp -= 1

        ans = min(ans, tmp)

print(ans)
