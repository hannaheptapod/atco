from math import gcd
a, b, c, d = map(int, input().split())
l = c * d // gcd(c, d)
def calc(n):
    mul = (n//c) + (n//d) - (n//l)
    return mul
mul = calc(b) - calc(a - 1)
ans = b - a + 1 - mul
print(ans)