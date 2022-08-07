from itertools import combinations

N, M = map(int, input().split())

for p in combinations(range(1, M+1), N): print(*p)
