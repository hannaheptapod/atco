N, M = map(int, input().split())
A = list(map(int, input().split()))

primes = set(i for i in range(2, M + 1) if all([i%j for j in range(2, int(i**0.5) + 1)]))

ans = [0] + [1]*M
for ai in A:
    rm = set()
    
    for p in primes:
        if ai%p: continue
        
        for pj in range(p, M + 1, p): ans[pj] = 0
        
        rm.add(p)
    
    for ri in rm: primes.remove(ri)

print(sum(ans))
_ = [print(i)  for i in range(1, M + 1) if ans[i]]
