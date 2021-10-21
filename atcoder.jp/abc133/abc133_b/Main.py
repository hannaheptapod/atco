n, d = map(int, input().split())
def dis(y, z):
    di = 0
    for i in range(d): di += (y[i] - z[i])**2
    for i in range(10**9):
        if i**2 < di: continue
        elif i**2 == di:
            return True
        else: return False
ans = 0
x = [list(map(int, input().split())) for _ in range(n)]
for i in range(n - 1):
    y = x[i]
    for j in range(i + 1, n):
        z = x[j]
        if dis(y, z): ans += 1
print(ans)