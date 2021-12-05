k, s = map(int, input().split())
per = (1, 3, 6)
ans = 0
for x in range(k + 1):
    for y in range(x, k + 1):
        z = s - x - y
        if z >= y and z <= k:
            ans += per[int(x < y) + int(y < z)]
print(ans)