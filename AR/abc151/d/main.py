h, w = map(int, input().split())
s = [input() for _ in range(h)]
maze = 0
for i in range(h):
    for j in range(w):
        maze <<= 1
        if s[i][j] == '.': maze += 1
