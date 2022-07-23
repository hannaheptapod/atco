N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j: continue

        st = set([A[i][j], A[j][i]])

        if 'D' in st and len(st) == 2 or 'D' not in st and len(st) == 1:
            ans = 'incorrect'
            break
    else: continue
    break
else: ans = 'correct'

print(ans)
