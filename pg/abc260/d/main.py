import bisect
from collections import deque

N, K = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))

ans = [-1]*N

decks = {}
tops = []
for i in range(N):
    pi = P[i]
    mj = bisect.bisect_left(tops, pi)
    if mj < len(tops):
        decks[tops[mj]].appendleft(pi)
        decks[pi] = decks[tops[mj]]
        del tops[mj]
    else: decks[pi] = deque([pi])

    bisect.insort(tops, pi)

    if len(decks[pi]) == K:
        for _ in range(K): ans[decks[pi].popleft()] = i+1
        tops.remove(pi)

print(*ans, sep='\n')
