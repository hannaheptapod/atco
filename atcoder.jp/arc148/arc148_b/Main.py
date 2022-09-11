import array

N = int(input())
S = array.array('i', [0 if si == 'd' else 1 for si in input()])

mn = S
for l in range(N):
    if not S[l]: continue

    arr = array.array('i')
    for r in range(l, N):
        arr.insert(0, int(not S[r]))
        if not S[r]: continue
        if arr+S[r+1:] < mn[l:]: mn = S[:l] + arr + S[r+1:]

    break

ans = ''.join('p' if mi else 'd' for mi in mn)
print(ans)
