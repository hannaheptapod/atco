R, C, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

ans = 0
for i in range(R):
    for j in range(C):
        if i+j > D or (i+j)%2 != D%2: continue

        ans = max(ans, A[i][j])

print(ans)
