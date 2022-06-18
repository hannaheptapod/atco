N = int(input())
X = list(map(lambda x: int(x)-1, input().split()))
C = list(map(int, input().split()))

checked = {i: False for i in range(N)}

ans = 0
for i in range(N):
    if checked[i]: continue
    checked[i] = True

    arr = [i]
    nxt = X[i]
    while not checked[nxt]:
        checked[nxt] = True
        arr.append(nxt)
        nxt = X[nxt]

    if nxt not in arr: continue
    id = arr.index(nxt)
    ans += min(C[a] for a in arr[id:])

print(ans)
