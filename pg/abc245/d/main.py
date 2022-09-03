N, M = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

b = [0]*(M+1)
for i in range(M, -1, -1):
    b[i] = c[N+i] // a[N]
    for j in range(N, -1, -1): c[i+j] -= b[i]*a[j]

print(*b)
