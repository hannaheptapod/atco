n = int(input())
csf = [list(map(int, input().split())) for _ in range(n-1)]

ans = [0]*n

for i in range(n-1):
    for j in range(i+1):
        if j == i or ans[j] <= csf[i][1]: ans[j] = csf[i][1]
        elif ans[j] % csf[i][2]: ans[j] += csf[i][2] - ans[j]%csf[i][2]
    for j in range(i+1): ans[j] += csf[i][0]

_ = [print(ai) for ai in ans]