n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
need = [False]*(n-1) + [True]
ans = a[-1][0]
for i in range(n-1, -1, -1):
    if need[i] and a[i][1]:
        for ai in a[i][2:]:
            if need[ai-1] == False: ans += a[ai-1][0]
            need[ai-1] = True
print(ans)