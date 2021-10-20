from math import gcd
a, b, c = map(int, input().split())
if c % gcd(a, b): ans = 'NO'
else: ans = 'YES'
print(ans)