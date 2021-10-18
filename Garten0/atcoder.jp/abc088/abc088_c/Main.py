c = [list(map(int, input().split())) for _ in range(3)]
da = [c[0][0] - c[1][0], c[1][0] - c[2][0]]
db = [c[0][0] - c[0][1], c[0][1] - c[0][2]]
ans = 'No'
for i in range(2):
    for j in range(2):
        if c[i][j+1] - da[i] == c[i+1][j+1] and c[i+1][j] - db[j] == c[i+1][j+1]: continue
        break
    else: continue
    break
else: ans = 'Yes'
print(ans)