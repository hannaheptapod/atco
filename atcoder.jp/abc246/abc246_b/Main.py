A, B = map(int, input().split())
ans = [A/(A**2 + B**2)**0.5, B/(A**2 + B**2)**0.5]
print(*ans)
