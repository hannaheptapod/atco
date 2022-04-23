from itertools import combinations

N, P = map(int, input().split())
A = 26

for i in range(N):
    tmp = len(list(combinations(range(1, N), i)))
    print(tmp)
