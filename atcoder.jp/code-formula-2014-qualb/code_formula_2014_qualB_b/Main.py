N = list(map(int, input()))[::-1]

ans = [0, 0]
for i in range(len(N)): ans[1-i%2] += N[i]

print(*ans)
