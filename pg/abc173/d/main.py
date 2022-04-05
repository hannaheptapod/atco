N = int(input())
A = sorted(map(int, input().split()), reverse=True)

ans = -A[0] + 2*sum(A[:N//2]) + (N % 2)*A[N//2]
print(ans)
