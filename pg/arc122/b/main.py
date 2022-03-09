N = int(input())
A = sorted(map(int, input().split()))

cusum = [0]
for ai in A: cusum.append(cusum[-1] + ai)

mn = cusum[-1]
for i in range(1, N + 1):
    x = A[i-1]/2
    tmp = cusum[-1] + N*x - (cusum[i] + (N-i)*2*x)
    
    mn = min(mn, tmp)

ans = mn/N

print(ans)
