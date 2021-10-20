n, a, b = map(int, input().split())
time = n // (a + b)
ans = a*time + min(a, n - time * (a + b))
print(ans)