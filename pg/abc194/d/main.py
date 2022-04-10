N = int(input())

ans = sum(N/k for k in range(1, N))
print(ans)
