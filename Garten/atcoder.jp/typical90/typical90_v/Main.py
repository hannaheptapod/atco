import math
a, b, c = map(int, input().split())
g1 = math.gcd(a, b)
g = math.gcd(g1, c)
ans = (a+b+c)//g - 3
print(ans)