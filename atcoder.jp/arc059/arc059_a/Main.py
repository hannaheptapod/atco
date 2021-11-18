n = int(input())
a = list(map(int, input().split()))
def cost(x, y): return (x - y)**2
a.sort()
ans = 10**10
for i in range(a[0], a[-1]+1): ans = min(ans, sum([cost(ai, i) for ai in a]))
print(ans)