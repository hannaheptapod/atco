n, h = map(int, input().split())
a, b = [], []
for _ in range(n):
    ab = list(map(int, input().split()))
    a.append(ab[0])
    b.append(ab[1])

amax = max(a)
bl = [bi for bi in b if bi > amax]
bl.sort(reverse=True)
ans = 0
sm = 0
for bli in bl:
    sm += bli
    ans += 1
    if sm >= h:
        break

if sm < h:
    ans += -((sm - h)//amax)

print(ans)