a, b, c = map(int, input().split())
ans = 'Yes' if b == sorted([a, b, c])[1] else 'No'
print(ans)
