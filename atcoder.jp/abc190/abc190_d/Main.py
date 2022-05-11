N = int(input())

ans = 0
for i in range(1, int((2*N)**0.5) + 1):
    if 2*N % i: continue

    if 2*N//i % 2 != i % 2: ans += 2

print(ans)
