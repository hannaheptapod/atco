n, q = map(int, input().split())
a = list(map(int, input().split()))
sh = 0
for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 0:
        print([a[(i + sh)%n] for i in range(n)])
    elif t == 1:
        ax, ay = a[(x-1 + sh)%n], a[(y-1 + sh)%n]
        a[(x-1 + sh)%n] = ay
        a[(y-1 + sh)%n] = ax
    elif t == 2:
        sh -= 1
    elif t == 3:
        print(a[(x-1 + sh)%n])