N = int(input())

ans = 0
for a in range(1, N + 1):
    if a**3 > N: break

    for b in range(a, N + 1):
        if a * b**2 > N: break

        ans += N//a//b - b + 1

print(ans)
