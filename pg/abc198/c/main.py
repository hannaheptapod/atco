r, x, y = map(int, input().split())
dst = pow(pow(x, 2) + pow(y, 2), 0.5)
ans = int(-(-dst//r))
if dst < r:
    ans = 2
print(ans)