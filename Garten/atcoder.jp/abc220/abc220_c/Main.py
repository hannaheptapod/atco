n = int(input())
a = list(map(int, input().split()))
sm = [0] * (n + 1)
for i in range(n):
    sm[i + 1] = sm[i] + a[i]
x = int(input())
s = sm[n]
t = x // s
k = n * t
x -= s * t

ng = -1
ok = n + 1
while ng + 1 < ok:
    md = (ng + ok) // 2
    if sm[md] > x: ok = md
    else: ng = md

ans = k + ok
print(ans)
