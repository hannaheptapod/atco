n, m = map(int, input().split())
abin = [list(map(int, input().split())) for _ in range(m)]
ab = []
for abi in abin:
    if abi not in ab: ab.append(abi)
ab.sort()
print(ab)
rng = [[0, n-1] for _ in range(n)]
for abi in ab:
    a, b = abi
    rng[a-1][1] -= 1
    rng[b-1][0] += 1
print(rng)