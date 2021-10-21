n = int(input())
h = list(map(int, input().split()))
ans = tmp = 0
for i in range(1, n):
    if h[i] <= h[i - 1]:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
ans = max(ans ,tmp)
print(ans)