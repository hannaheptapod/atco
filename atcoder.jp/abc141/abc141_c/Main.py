n, k, q = map(int, input().split())
p = [0]*n
for _ in range(q): p[int(input()) - 1] += 1
for pi in p:
    if k + pi - q > 0: print('Yes')
    else: print('No')