import itertools
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = []
for _ in range(m):
    x, y = map(int, input().split())
    xy += (x-1, y-1), (y-1, x-1)
arr = tuple(range(n))
parr = itertools.permutations(arr)
ans = 10001
for p in parr:
    tmp = a[p[0]][0]
    for i in range(n - 1):
        if p[i:i+2] in xy:
            break
        else:
            tmp += a[p[i+1]][i+1]
    else:
        if tmp < ans:
            ans = tmp
if ans == 10001:
    ans = -1
print(ans)

