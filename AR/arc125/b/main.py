from math import ceil
n = int(input())
mod = 998244353
ans = 0
root_n = n ** 0.5
for q in range(1, ceil(root_n) + 1):
    ans = (ans + (n/q - q) // 2 + 1) % mod
print(int(ans))