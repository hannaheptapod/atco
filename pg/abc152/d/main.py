N = int(input())

l = [[0]*10 for _ in range(10)]
for i in range(1, N + 1): l[int(str(i)[0])][int(str(i)[-1])] += 1

ans = sum([l[i][j]*l[j][i] for i in range(1, 10) for j in range(1, 10)])

print(ans)