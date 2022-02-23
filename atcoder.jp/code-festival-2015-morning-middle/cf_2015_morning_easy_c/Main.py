N, K, M, R = map(int, input().split())
S = [int(input()) for _ in range(N-1)]
S.sort(reverse=True)

if sum(S[:K]) >= K*R: ans = 0
elif sum(S[:K-1])+M < K*R: ans = -1
else: ans = K*R - sum(S[:K-1])

print(ans)