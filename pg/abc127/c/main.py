n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]
ans = max(0, min([lr[i][1] for i in range(m)]) - max([lr[i][0] for i in range(m)]) + 1)
print(ans)