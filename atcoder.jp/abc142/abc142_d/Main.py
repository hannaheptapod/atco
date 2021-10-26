import math
a, b = map(int, input().split())
g = math.gcd(a, b)
div = set()
for i in range(2, -int(-g**0.5//1) + 1):
    if not g % i:
        div.add(i)
        while not g % i: g //= i
div.add(g)
div.add(1)
print(len(div))