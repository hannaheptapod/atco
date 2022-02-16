n = int(input())

mod = 998244353

mx = len(str(n))
ans = 0

for i in range(1, mx+1):
    if n >= 10**i-1: tmp = (1 + 9*10**(i-1))*(9*10**(i-1))//2
    else: tmp = (1 + n - 10**(i-1) + 1)*(n - 10**(i-1) + 1)//2

    ans = (ans + tmp)%mod

print(ans)