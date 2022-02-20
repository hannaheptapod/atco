from bisect import bisect

H, W = map(int, input().split())
map = [input() for _ in range(H)]

ver = [[-1]+[i for i in range(H) if map[i][j] == '#']+[H] for j in range(W)]
hor = [[-1]+[j for j in range(W) if map[i][j] == '#']+[W] for i in range(H)]

ans = 0
for i in range(H):

    for j in range(W):
        if map[i][j] == '#': continue
        
        u, d = ver[j][bisect(ver[j], i)-1], ver[j][bisect(ver[j], i)]
        l, r = hor[i][bisect(hor[i], j)-1], hor[i][bisect(hor[i], j)]

        tmp = (d - u - 1) + (r - l - 1) - 1
        ans = max(ans, tmp)

print(ans)