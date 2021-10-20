n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
pt = [ab[i][1] for i in range(n)]
pt += [ab[i][0] - ab[i][1] for i in range(n)]
pt.sort(reverse=True)
ans = sum(pt[:k])
print(ans)