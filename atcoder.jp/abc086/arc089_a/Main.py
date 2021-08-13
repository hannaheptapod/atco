n = int(input())
t, x, y = 0, 0, 0
ans = 'Yes'
for _ in range(n):
    ti, xi, yi = map(int, input().split())
    dt = ti - t
    dx = abs(xi - x)
    dy = abs(yi - y)
    tmp = dt - (dx + dy)
    if tmp < 0 or tmp % 2 == 1:
        ans = 'No'
        break
    else:
        t = ti
        x = xi
        y = yi
print(ans)