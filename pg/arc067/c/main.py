n = int(input())
mod = 10**9 + 7

p = [2] + [i for i in range(3, n+1, 2) if all([i%j for j in range(3, int(i**0.5) + 1, 2)])]

ans = 1

for pi in p:
    f = 1
    tmp = n

    while tmp:
        tmp //= pi
        f += tmp
    
    ans = ans*f % mod

print(ans)