def main():
    N = int(input())
    M = 55555

    primes = get_primes(M)
    mods = [[] for _ in range(5)]
    for p in primes: mods[p%5].append(p)

    for m in mods:
        if len(m) < N: continue
        ans = m[:N]
        break

    print(*ans)


def get_primes(M):
    is_prime = [True] * (M + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, M + 1):
        if is_prime[i]:
            for j in range(i * 2, M + 1, i):
                is_prime[j] = False
    return [i for i in range(M + 1) if is_prime[i]]


if __name__ == '__main__': main()
