N, K = map(int, input().split())

ans = sum([6*(K-1)*(N-K), 3*(N-1), 1]) / N**3
print(ans)
