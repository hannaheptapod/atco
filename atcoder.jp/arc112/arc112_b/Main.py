B, C = map(int, input().split())

l = B - C//2
if C < 2: r = B
else: r = B + (C - 2)//2

p = -B - (C - 1)//2
q = -B + (C - 1)//2

ans = r-l+1 + q-p+1
u = max(l, p)
v = min(r, q)
if u <= v: ans -= v-u+1

print(ans)
