N = int(input())


def sieve_eratosthenes(n):
    primes = [0, 1] * (n // 2 + 1)
    if not n%2: primes.pop()
    primes[1], primes[2] = 0, 1
    for p in range(3, int(n ** 0.5) + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p): primes[q] = 0
    return primes


primes = sieve_eratosthenes(10**6)

tot = [0]
for pi in primes[1:]: tot.append(tot[-1] + pi)

ans = 0
for q in range(10**6+1):
    if 2 * q**3 > N: break
    if not primes[q]: continue

    ans += tot[min(q-1, N//(q**3))]

print(ans)
