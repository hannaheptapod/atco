import array

N, X = map(int, input().split())

if X < N//2: per = array.array('i', [X, (N+X)//2, (N+X)//2+1])
elif X == N//2: per = array.array('i', [X, X+1])
elif X == N//2 + 1: per = array.array('i', [X, X-1])
else: per = array.array('i', [X, X//2, X//2+1])
used = [False]*(N+1)
for pi in per: used[pi] = True

for _ in range(N-len(per)):
    d = abs(per[-1]-per[-2])

    for i in range(d+1, N):
        if per[-1]-i <= 0 and per[-1]+i > N: break

        if per[-1] <= N//2:
            if per[-1]+i <= N and not used[per[-1]+i]:
                per.append(per[-1]+i)
                used[per[-1]] = True
                break
            elif per[-1]-i > 0 and not used[per[-1]-i]:
                per.append(per[-1]-i)
                used[per[-1]] = True
                break
            else: continue
        else:
            if per[-1]-i > 0 and not used[per[-1]-i]:
                per.append(per[-1]-i)
                used[per[-1]] = True
                break
            elif per[-1]+i <= N and not used[per[-1]+i]:
                per.append(per[-1]+i)
                used[per[-1]] = True
                break
            else: continue

for i in range(1, N+1):
    if not used[i]: per.append(i)

print(*per)
