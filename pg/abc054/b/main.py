n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        for y in range(m):
            for x in range(m):
                if a[i + y][j + x] != b[y][x]: break
            else: continue
            break
        else:
            ans = 'Yes'
            break
    else: continue
    break
else: ans = 'No'
print(ans)