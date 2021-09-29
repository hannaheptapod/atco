n, k, l = map(int, input().split())
pq = [list(map(int, input().split())) for _ in range(k)]
rs = [list(map(int, input().split())) for _ in range(l)]

dp = [[0]]