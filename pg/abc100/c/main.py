n = int(input())
a = list(map(int, input().split()))
ans = 0
for ai in a:
    while ai%2 == 0:
        ans += 1
        ai //= 2
print(ans)