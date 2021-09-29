x, a, b = map(int, [input() for _ in range(3)])
x -= a
x -= b * (x // b)
print(x)