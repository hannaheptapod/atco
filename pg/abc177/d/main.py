from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = [set() for _ in range(N + 1)]
for abi in AB:
    a, b = abi
    G[a].add(b)
    G[b].add(a)

d = deque([1])
cnt = 0
