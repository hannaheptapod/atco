import array

N, X = map(int, input().split())

per = array.array('i', [X, X+1] if X <= N//2 else [X, X-1])
used = [False]*(N+1)
used[per[0]] = used[per[1]] = True

for _ in range(N-2):
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

if len(per) < max(X-1, N-X):
    per = array.array('i', [
        X, (X-1)//2, (X-1)//2+1]
        if X-1 >= N-X else
        [X, (N+X+1)//2, (N+X+1)//2+1])

    used = [False]*(N+1)
    for p in per: used[p] = True

    for _ in range(N-3):
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
