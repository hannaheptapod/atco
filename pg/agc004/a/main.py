a, b, c = map(int, input().split())
ans = min(a%2*b*c, b%2*c*a, c%2*a*b)
print(ans)