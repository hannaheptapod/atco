n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab.sort()

ans = min(n, m)
print(ans)