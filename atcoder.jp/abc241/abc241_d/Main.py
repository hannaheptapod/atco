import array
from bisect import insort, bisect_left, bisect_right

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

s = sorted(set(q[1] for q in query))
xtoy = {s[i]: i for i in range(len(s))}
ytox = {i: s[i] for i in range(len(s))}

arr = array.array('i')
for q in query:
    if q[0] == 1: insort(arr, xtoy[q[1]])
    elif q[0] == 2:
        id = bisect_right(arr, xtoy[q[1]]) - q[2]
        print(ytox[arr[id]] if id >= 0 else -1)
    else:
        id = bisect_left(arr, xtoy[q[1]]) + q[2] - 1
        print(ytox[arr[id]] if id < len(arr) else -1)
