n = int(input())
a = list(map(int, input().split()))
sm = [[0]*n for _ in range(2)]
sm[0][0], sm[1][0] = a[0], sum(a)
for i in range(1, n):
    sm[0][i], sm[1][i] = sm[0][i-1]+a[i], sm[1][i-1]-a[i-1]
ans = min([abs(sm[0][i]-sm[1][i+1]) for i in range(n-1)])
print(ans)