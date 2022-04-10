N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
b = ''.join(str(int(A[i] < A[i+1])) for i in range(N-1))
c = list(b.split('0'))

ans = sum(max(0, len(ci) - K + 2) for ci in c)
print(ans)
