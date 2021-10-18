n, l = map(int, input().split())
sum = 0
tmp = 500
for i in range(n):
    t = l + i
    sum += t
    if abs(t) < abs(tmp): tmp = t
ans = sum - tmp
print(ans)