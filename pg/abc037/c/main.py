N, K = map(int, input().split())
a = list(map(int, input().split()))
b = [min(i+1, N-i, K, N-K+1) for i in range(N)]

ans = sum([a[i]*b[i] for i in range(N)])
print(ans)
