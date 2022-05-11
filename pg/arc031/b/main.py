from collections import deque
from itertools import product

A = [input() for _ in range(10)]

for i in range(10):
    for j in range(10):
        if A[i][j] == 'o': continue

        seen = {(y, x): A[y][x] == 'x' and (y, x) != (i, j)
                for (y, x) in product(range(10), repeat=2)}

        deq = deque([(i, j)])
        while deq:
            y, x = deq.popleft()
            if seen[(y, x)]: continue
            seen[(y, x)] = True

            if y > 0: deq.append((y-1, x))
            if y < 9: deq.append((y+1, x))
            if x > 0: deq.append((y, x-1))
            if x < 9: deq.append((y, x+1))

        if all(seen.values()):
            ans = 'YES'
            break
        continue

    else: continue
    break
else: ans = 'NO'

print(ans)
