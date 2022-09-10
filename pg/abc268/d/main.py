from itertools import combinations, permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))
L = sum(len(si) for si in S)

if N == 1: ans = S[0] if L >= 3 and S[0] not in T else -1
else:
    for c in combinations(range(1, 16-L+1), N-1):
        bar = [c[0]] + [c[i+1]-c[i] for i in range(N-2)]

        for p in permutations(S, N):
            tmp = p[0]
            for i in range(N-1):
                tmp += '_'*bar[i] + p[i+1]

            if tmp not in T:
                ans = tmp
                break
        else: continue
        break
    else: ans = -1

print(ans)
