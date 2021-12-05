from math import pi, atan
a, b, x = map(int, input().split())
if x*2 >= a**2 * b:
    s = a*b - x/a
    t = 2*s / a
    ans = 180*atan(t/a) / pi
else:
    s = x/a
    t = 2*s / b
    ans = 90 - 180*atan(t/b) / pi
print(ans)