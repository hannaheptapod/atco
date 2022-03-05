L, X, Y, S, D = map(int, input().split())

if S <= D: K = D-S
else: K = D-S + L

if X < Y: ans = min(K/(X+Y), (L-K)/(Y-X))
else: ans = K/(X+Y)

print(ans)
