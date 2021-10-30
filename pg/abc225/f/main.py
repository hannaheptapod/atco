n, k = map(int, input().split())
ss = [input() for _ in range(n)]
ss.sort()
ans = ''.join(ss[:k])
print(ans)