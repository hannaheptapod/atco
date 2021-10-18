a, b, c = map(int, input().split())
dd = 2*b - a - c
k = max(0, (1 - dd)//2)
print(dd + 3*k)