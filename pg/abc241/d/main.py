import bisect
from array import array

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
a = array('l', [])
leng = 0

for qi in query:
    if qi[0] == 1:
        bisect.insort(a, qi[1])
        leng += 1
        continue

    if qi[0] == 2:
        id = bisect.bisect_right(a, qi[1])
        if id - qi[2] >= 0: print(a[id - qi[2]])
        else: print(-1)
    
    if qi[0] == 3:
        id = bisect.bisect_left(a, qi[1])
        if id-1 + qi[2] < leng: print(a[id-1 + qi[2]])
        else: print(-1)