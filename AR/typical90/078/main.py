n, m = map(int, input().split())

p = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    p[max(a, b)] += 1

ans = sum([pi == 1 for pi in p])

print(ans)