N = int(input())
A = [input() for _ in range(N)]
for i in range(N): A[i] = A[i]*3
A = A*3

ans = -1
for i in range(N, 2*N):
    for j in range(N, 2*N):
        for di, dj in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
            ans = max(ans, int(''.join(A[i+k*di][j+k*dj] for k in range(N))))

print(ans)
