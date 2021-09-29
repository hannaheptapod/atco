n = int(input())
abcde = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
dp = [[[0, 0, 0, 0, 0] for _ in range(4)] for _ in range(n)]

