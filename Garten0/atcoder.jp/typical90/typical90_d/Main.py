h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
sumr = [sum(a[row]) for row in range(h)]
sumc = [sum([a[row][col] for row in range(h)]) for col in range(w)]
ans = [[sumr[row] + sumc[col] - a[row][col] for col in range(w)] for row in range(h)]
for row in range(h):
    print(*ans[row])