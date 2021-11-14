from math import gcd
def lcm(n1, n2): return n1*n2//gcd(n1, n2)
n = int(input())
ans = 1
for _ in range(n): ans = lcm(ans, int(input()))
print(ans)