n = int(input())
ans = 0
if not n % 2:
    m = n // 2
    while m:
        m //= 5
        ans += m
print(ans)