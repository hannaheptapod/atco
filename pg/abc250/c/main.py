N, Q = map(int, input().split())
dic, inv = [{i: i for i in range(1, N+1)} for _ in range(2)]

for _ in range(Q):
    x = int(input())
    dx = dic[x]

    dy = dx+1 if dx < N else dx-1
    y = inv[dy]

    dic[x], dic[y] = dy, dx
    inv[dx], inv[dy] = y, x

ans = [inv[i] for i in range(1, N+1)]
print(*ans)
