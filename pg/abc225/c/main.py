n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
b0 = b[0][0]
if (b0%7 == 0 and m > 1) or (b0%7 > 0 and b0%7 > 8 - m): ans = 'No'
else:
    for i in range(n):
        for j in range(m):
            if b[i][j] != b0 + i*7 + j:
                ans = 'No'
                break
            else: continue
        else: continue
        break
    else: ans = 'Yes'
print(ans)