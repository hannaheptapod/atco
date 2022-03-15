N = int(input())
x = [input() for _ in range(N)]

ans = 0
for j in range(9):
    prev = ''
    for i in range(N):
        if x[i][j] == 'x': ans += 1
        elif prev != 'o' and x[i][j] == 'o': ans += 1

        prev = x[i][j]

print(ans)
