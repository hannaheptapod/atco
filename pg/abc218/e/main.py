from heapq import heappop, heappush

N, M = map(int, input().split())
ABC = [list(map(int, input().split()))for _ in range(M)]

graph = [[] for _ in range(N)]
