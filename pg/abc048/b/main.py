a, b, n = map(int, input().split())
ans = b // n - (a - 1) // n
print(ans)