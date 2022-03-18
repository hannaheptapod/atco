H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(lambda x: abs(int(x)), input().split())) for _ in range(H)]

for k in range(10):
    for i in range(10):
        for j in range(10): c[i][j] = min(c[i][j], c[i][k] + c[k][j])

ans = sum([sum([c[aij][1] for aij in ai]) for ai in A])
print(ans)
