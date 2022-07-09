N, M, X, T, D = map(int, input().split())

ans = T - D*X + D*min(M, X)
print(ans)
