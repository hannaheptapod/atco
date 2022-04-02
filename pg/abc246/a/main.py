xy = [list(map(int, input().split())) for _ in range(3)]
if xy[0][0] == xy[1][0]: ax = xy[2][0]
elif xy[1][0] == xy[2][0]: ax = xy[0][0]
else: ax = xy[1][0]
if xy[0][1] == xy[1][1]: ay = xy[2][1]
elif xy[1][1] == xy[2][1]: ay = xy[0][1]
else: ay = xy[1][1]

print(ax, ay)
