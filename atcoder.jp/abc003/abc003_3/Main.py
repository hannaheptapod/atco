N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

ans = 0
for ri in R[N-K:]: ans = (ans + ri)/2

print(ans)