import array
import bisect
from collections import deque

a, b = array.array('i', []), deque()
Q = int(input())
for _ in range(Q):
    c = list(map(int, input().split()))

    if c[0] == 1: b.append(c[1])
    if c[0] == 2: print(a.pop(0) if a else b.popleft())
    if c[0] == 3:
        while b: bisect.insort(a, b.popleft())
