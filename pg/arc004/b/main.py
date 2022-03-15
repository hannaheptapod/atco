N = int(input())
d = [int(input()) for _ in range(N)]
d.sort()

mx = sum(d)
mn = max(2*d[-1] - mx, 0)

print(*[mx, mn], sep='\n')
