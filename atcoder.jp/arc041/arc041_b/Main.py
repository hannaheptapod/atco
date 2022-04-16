N, M = map(int, input().split())
b = [list(map(int, input())) for _ in range(N)]

a = [[0]*M for _ in range(N)]
dr = ((0, 0), (1, -1), (1, 1), (2, 0))

for i in range(N-2):
    for j in range(1, M-1):
        bij = b[i][j]

        a[i+1][j] += bij
        for dy, dx in dr: b[i+dy][j+dx] -= bij

ans = [''.join(map(str, ai)) for ai in a]
print(*ans, sep='\n')
