h, n = map(int, input().split())
l_mg = [list(map(int, input().split())) for _ in range(n)]
for i in range(n): l_mg[i] = [l_mg[i][0]/l_mg[i][1]] + l_mg[i]
l_mg.sort(reverse=True)

ans = -(-h//l_mg[0][1])*l_mg[0][2]

print(ans)