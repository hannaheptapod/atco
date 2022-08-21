H, W = map(int, input().split())
G = [input() for _ in range(H)]

seen = [[0]*W for _ in range(H)]

flag = 1
y, x = 0, 0
while not seen[y][x]:
    seen[y][x] = 1

    if G[y][x] == 'U' and y: y -= 1
    elif G[y][x] == 'D' and y < H-1: y += 1
    elif G[y][x] == 'L' and x: x -= 1
    elif G[y][x] == 'R' and x < W-1: x += 1
    else: break

    if seen[y][x]:
        flag = 0
        break

ans = [y+1, x+1] if flag else [-1]
print(*ans)
