import numpy as np
from itertools import product

N, M, X = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(N)])

arr_s = np.sum(A, axis=0)
if min(arr_s[1:]) < X: ans = -1
else:
    ans = arr_s[0]

    for p in product((0, 1), repeat=N):
        arr_p = np.reshape(np.array(p), (1, N))

        tmp = np.sum(np.dot(arr_p, A), axis=0)
        if min(tmp[1:]) < X: continue

        ans = min(ans, tmp[0])

print(ans)
