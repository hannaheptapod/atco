import array

N, X = map(int, input().split())

if X == -int(-N//2): per = array.array('i', [X, X+1])
used = [False]*(N+1)
for pi in per: used[pi] = True

for _ in range(N-len(per)):
    d = per[-1]-per[-2]
    if d > 0: per.append(per[-1]-d-1 if not used[per[-1]-d-1] else per[-1]-d-2)
    else: per.append(per[-1]-d+1 if not used[per[-1]-d+1] else per[-1]-d+2)
    used[per[-1]] = True

print(*per)
