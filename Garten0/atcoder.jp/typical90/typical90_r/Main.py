import decimal
import math
from decimal import Decimal

t = int(input())
l, x, y = map(int, input().split())
ll = Decimal(l)
xt, yt, zt = Decimal(x), Decimal(y), Decimal(0)

q = int(input())
for _ in range(q):
    e = Decimal(input())
    xi = Decimal(0)
    theta = 2 * Decimal(math.pi) * e / t
    yi = (ll/2) * Decimal(-math.sin(theta))
    zi = ll/2 + (ll/2) * Decimal(-math.cos(theta))
    d_xy = ((xi-xt)*(xi-xt) + (yi-yt)*(yi-yt)).sqrt()
    d_z = zi - zt
    ans = math.degrees(math.atan(float(d_z/d_xy)))
    print(ans)