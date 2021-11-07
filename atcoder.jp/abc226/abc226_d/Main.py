from math import gcd
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
vec = set()
for i in range(n-1):
    xi, yi = xy[i]
    for j in range(i+1, n):
        xj, yj = xy[j]
        if xi == xj: vec.add('y')
        elif yi == yj: vec.add('x')
        else:
            g = gcd(xi-xj, yi-yj)
            vec.add(((-1)**int(xi-xj < 0)*(xi-xj)//g, (-1)**int(xi-xj < 0)*(yi-yj)//g))
print(len(vec)*2)