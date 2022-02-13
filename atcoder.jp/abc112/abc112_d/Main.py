n, m = map(int, input().split())

ans = 1

for i in range(m//n, 0, -1):
    if m%i == 0:
        ans = i
        break

print(ans)