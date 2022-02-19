a, b, c, d = map(int, input().split())

primes = [2] + [i for i in range(3, 200, 2) if all([i%j for j in range(2, int(i**0.5) + 1)])]

for tak in range(a, b + 1):
    for aok in range(c, d + 1):
        if tak+aok in primes: break
    else:
        ans = 'Takahashi'
        break
else: ans = 'Aoki'

print(ans)