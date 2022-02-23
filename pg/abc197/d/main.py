import math

N = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
xc, yc = (x0 + x1)/2, (y0 + y1)/2

theta = 2*math.pi / N

ans = (
    xc + math.cos(theta)*(x0 - xc) - math.sin(theta)*(y0 - yc),
    yc + math.sin(theta)*(x0 - xc) + math.cos(theta)*(y0 - yc)
    )

print(*ans)