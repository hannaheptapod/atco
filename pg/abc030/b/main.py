n, m = map(int, input().split())

s, l = 30*(n % 12) + 0.5*m, 6*m

ans = min((s-l)%360, (l-s)%360)
print(ans)
