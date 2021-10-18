n = int(input())
cp = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

sm = [[0]*2 for _ in range(n+1)]

for i in range(n):
    c, p = cp[i]
    for j in range(2):
        sm[i+1][j] = sm[i][j]
    sm[i+1][c-1] += p

for i in range(q):
    l, r = lr[i]
    ans = [sm[r][j] - sm[l-1][j] for j in range(2)]
    print(*ans)