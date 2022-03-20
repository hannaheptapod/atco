N = int(input())
S = input()

pos = [0, 0]
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)
cnt = 0

for si in S:
    if si == 'S': pos = pos[0]+dx[cnt%4], pos[1]+dy[cnt%4]
    else: cnt += 1

print(*pos)
