n = int(input())
t = list(map(int, input().split()))
sm = sum(t)
m = int(input())
for _ in range(m):
    p, x = map(int, input().split())
    print(sm - t[p-1] + x)