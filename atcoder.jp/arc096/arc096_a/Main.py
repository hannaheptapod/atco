a, b, c, x, y = map(int, input().split())
ans = a*x + b*y
while x > 0 or y > 0:
    ans = min(ans, ans - int(x > 0)*a - int(y > 0)*b + 2*c)
    x -= 1
    y -= 1
print(ans)