n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    sm = sum([ai * bi for ai, bi in zip(a, b)]) + c
    if sm > 0: ans += 1
print(ans)