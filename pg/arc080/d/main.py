h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

c = []
for i in range(n): c += [i+1]*a[i]
ans = [c[i*w:(i+1)*w:1] for i in range(h)]
for i in range(1, h, 2): ans[i] = ans[i][::-1]

_ = [print(*ai) for ai in ans]