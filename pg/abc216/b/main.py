n = int(input())
st = [list(input().split()) for _ in range(n)]
ans = 'No'
for i in range(n-1):
    si = st[i][0]
    ti = st[i][1]
    for j in range(i+1, n):
        if si == st[j][0]:
            if ti == st[j][1]:
                ans = 'Yes'
                break
            else: continue
        else: continue

print(ans)