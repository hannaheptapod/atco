def e(x): return x*(x+1) / (2*x)
n, k = map(int, input().split())
p = list(map(lambda x: e(int(x)), input().split()))
sm = sum(p[:k])
ans = sm
for i in range(n-k):
    sm += p[i+k] - p[i]
    ans = max(ans, sm)
print(ans)