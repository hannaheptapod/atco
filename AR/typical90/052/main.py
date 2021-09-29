n = int(input())
mod = 10**9 + 7
ans = 1
for _ in range(n):
    a = list(map(int, input().split()))
    sum = 0
    for ai in a:
        sum += ai
    ans = (ans * sum) % mod
print(ans)