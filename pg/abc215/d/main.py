N, M = map(int, input().split())
A = list(map(int, input().split()))

spf = [i for i in range(max(A)+1)]
for i in range(2, int(max(A)**0.5)+1):
    if spf[i] == i:
        for j in range(i**2, max(A)+1, i):
            if spf[j] == j: spf[j] = i

primes = set()
for ai in A:
    while ai > 1:
        primes.add(spf[ai])
        ai //= spf[ai]

ans = set([i for i in range(1, M+1)])
for p in primes:
    for i in range(p, M+1, p): ans.discard(i)

ans = sorted(ans)
print(len(ans))
_ = [print(ai) for ai in ans]
