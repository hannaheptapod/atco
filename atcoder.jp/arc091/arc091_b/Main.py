N, K = map(int, input().split())

ans = sum([(N//b)*(b-K) + max(0, N%b - K + int(K > 0)) for b in range(K+1, N + 1)])

print(ans)