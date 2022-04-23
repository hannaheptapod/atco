from itertools import product

N, K = map(int, input().split())
S = [input() for _ in range(N)]

mat = [[chr(ord('a') + j) in S[i] for j in range(26)] for i in range(N)]

ans = 0
for pd in product(range(2), repeat=N):
    if sum(pd) < K: continue
    tmp = 0

    for a in range(26):
        chr_a = chr(ord('a') + a)
        cnt = 0

        for i in range(N):
            if not pd[i]: continue

            cnt += 1 if chr_a in S[i] else 0

        if cnt == K: tmp += 1

    ans = max(ans, tmp)

print(ans)
