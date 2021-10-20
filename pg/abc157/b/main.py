a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
card = [[0, 0, 0] for _ in range(3)]
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b: card[i][j] = 1

ans = 'No'
if any([all([card[i][j] for j in range(3)]) for i in range(3)] + [all([card[i][j] for i in range(3)]) for j in range(3)] + [all([card[i][i] for i in range(3)])] + [all([card[i][2-i] for i in range(3)])]): ans = 'Yes'
print(ans)