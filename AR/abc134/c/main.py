n = int(input())
a = [int(input()) for _ in range(n)]
sa = sorted(a)
for ai in a:
    if ai == sa[-1]: print(sa[-2])
    else: print(sa[-1])