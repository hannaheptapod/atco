N, M = map(int, input().split())
S = [sum(list(map(int, list(input())))) for _ in range(N)]

cnt = [0]*2
for si in S: cnt[si%2] += 1

ans = cnt[0]*cnt[1]
print(ans)
