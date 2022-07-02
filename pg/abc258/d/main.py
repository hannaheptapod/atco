N, X = map(int, input().split())
AB = [list(map(int, input().split()))+[0, 0] for _ in range(N)]

for i in range(N):
    AB[i][2] = sum(AB[i][:2])
    AB[i][3] = AB[i-1][3] + AB[i][2] if i > 0 else AB[i][2]

ans = min(AB[i][3]+AB[i][1]*(X-i-1) for i in range(min(X, N)))
print(ans)
