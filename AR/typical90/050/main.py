n, l = map(int, input().split())
mod = 10**9 + 7
stp = [1]*l

for i in range(n - l + 1):
    stp[i % l] = (stp[i % l] + stp[(i - 1) % l]) % mod
ans = stp[(n) % l]

print(ans)