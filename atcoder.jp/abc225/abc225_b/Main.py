n = int(input())
g = [0]*n
for _ in range(n-1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a] += 1
    g[b] += 1
for gi in g:
    if gi != 1 and gi != n-1:
        ans = 'No'
        break
    else: continue
else: ans = 'Yes'
print(ans)