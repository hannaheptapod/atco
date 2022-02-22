N = int(input())
A = list(map(int, input().split()))
for i in range(N): A[i] -= i

sor_a = sorted(A)
if N%2: md = sor_a[N//2]
else: md = (sor_a[N//2 - 1] + sor_a[N//2]) // 2

ans = sum([abs(ai-md) for ai in A])
print(ans)