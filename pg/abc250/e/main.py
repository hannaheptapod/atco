import array
from bisect import bisect_left as bil

N = int(input())
A = array.array('i', map(int, input().split()))
B = array.array('i', map(int, input().split()))
Q = int(input())
xy = [list(map(int, input().split())) for _ in range(Q)]

s = sorted(set(A + B))
a = array.array('i', [bil(s, ai) for ai in A])
b = array.array('i', [bil(s, bi) for bi in B])
