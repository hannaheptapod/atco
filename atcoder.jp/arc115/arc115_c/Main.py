N = int(input())

l_pr = [i for i in range(2, N+1) if all([i % j for j in range(2, int(i**0.5)+1)])]
ans = [1]*N
for i in range(1, N+1):
    tmp = i
    for p in l_pr:
        if tmp < p: break

        while tmp % p == 0:
            tmp //= p
            ans[i-1] += 1

print(*ans)
