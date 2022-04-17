N, K = map(lambda x: abs(int(x)), input().split())

num = [0]*2 + [min(x - 1, 2*N + 1 - x) for x in range(2, 2*N + 1)]

ans = sum(num[x]*num[x-K] for x in range(K, 2*N + 1))
print(ans)
