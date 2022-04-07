n, X = map(int, input().split())
a = list(map(int, input().split()))

ans = sum([a[i] for i in range(n) if 1<<i & X])
print(ans)
