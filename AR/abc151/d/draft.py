from collections import deque
h, w = map(int, input().split())
s = [input() for _ in range(h)]

def search(maze, i, j, seen, ii, jj, depth):
    if maze[i][j] == '#' or [i, j] in seen: return 401
    elif (i, j) == (ii, jj): return depth
    else:
        seen.append([i, j])
        ds = [401]*4
        if i > 0: ds[0] = search(maze, i-1, j, seen, ii, jj, depth+1)
        if i < h-1: ds[1] = search(maze, i+1, j, seen, ii, jj, depth+1)
        if j > 0: ds[2] = search(maze, i, j-1, seen, ii, jj, depth+1)
        if j < w-1: ds[3] = search(maze, i, j+1, seen, ii, jj, depth+1)
        return min(ds)

ans = 0
for i in range(h):
    for j in range(w):
        for ii in range(h):
            for jj in range(w):
                d = search(s.copy(), i, j, [], ii, jj, 0)
                if d < 401 and d > ans: ans = d
print(ans)