n = int(input())
a = list(map(int, input().split()))
sm = sum(a)
for i in range(1, n): a[i] += a[i-1]
ans = 10**100
for i in range(n-1): ans = min(ans, abs(2*a[i] - sm))
print(ans)