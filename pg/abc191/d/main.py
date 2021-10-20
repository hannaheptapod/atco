import math
def distance(x, y):
    dist_sq = x**2 + y**2
    return dist_sq
X, Y, R = map(10**4*float, input().split())
xmin, xmax = math.floor(X - R), math.ceil(X + R)
