n = int(input())
a = [0] + list(map(int, input().split())) + [0]
sm = sum([abs(a[i+1]-a[i]) for i in range(n+1)])
for i in range(n):
    ans = sm - abs(a[i+1]-a[i]) - abs(a[i+2]-a[i+1]) + abs(a[i+2]-a[i])
    print(ans)