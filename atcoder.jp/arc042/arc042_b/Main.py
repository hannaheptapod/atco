x, y = map(int, input().split())
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
board.append(board[0])

ans = 10**3
for i in range(N):
    x1, y1 = board[i]
    x2, y2 = board[i+1]

    d = abs((y2-y1)*x - (x2-x1)*y - (x1*y2-x2*y1))/((x2-x1)**2+(y2-y1)**2)**0.5
    ans = min(ans, d)

print(ans)
