ax, ay, bx, by, T, V = map(int, input().split())
n = int(input())


def dist(x, y): return sum(((tx - x)**2 + (ty - y)**2)**0.5 for tx, ty in ((ax, ay), (bx, by)))


ans = 'NO'
for _ in range(n):
    x, y = map(int, input().split())
    if dist(x, y) <= T*V: ans = 'YES'

print(ans)
