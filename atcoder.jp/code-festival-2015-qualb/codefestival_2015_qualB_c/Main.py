N, M = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)

ans = 'YES' if N >= M and all([A[i] >= B[i] for i in range(M)]) else 'NO'
print(ans)
